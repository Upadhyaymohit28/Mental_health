from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date, timedelta
from moodtracking.models import MoodLog
from gamification.models import Badge, Streak

@receiver(post_save, sender=MoodLog)
def update_streak(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        streak, _ = Streak.objects.get_or_create(user=user)

        # Check if the mood log is on the same day
        if streak.last_activity_date == date.today():
            # Do nothing; the user already logged today
            return

        # Check if the mood log is consecutive
        if streak.last_activity_date == date.today() - timedelta(days=1):
            streak.current_streak += 1
        else:
            streak.current_streak = 1

        # Update the longest streak if needed
        streak.longest_streak = max(streak.longest_streak, streak.current_streak)

        # Update last_activity_date to today
        streak.last_activity_date = date.today()
        streak.save()

        # Award badges based on streak milestones
        award_badges(user, streak.current_streak)

def award_badges(user, current_streak):
    """
    Award badges based on the user's current streak milestones.
    """
    badge_milestones = [
        (3, "3-Day Streak", "Logged mood for 3 consecutive days."),
        (7, "7-Day Streak", "Logged mood for 7 consecutive days."),
        (14, "14-Day Streak", "Logged mood for 14 consecutive days."),
        (30, "30-Day Streak", "Logged mood for 30 consecutive days."),
        (100, "100-Day Streak", "Logged mood for 100 consecutive days."),
    ]

    for days, name, description in badge_milestones:
        if current_streak >= days:
            Badge.objects.get_or_create(
                user=user,
                name=name,
                defaults={"description": description}
            )