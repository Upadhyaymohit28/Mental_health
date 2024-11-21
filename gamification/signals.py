from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date, timedelta
from moodtracking.models import MoodLog
from .models import Badge, Streak


@receiver(post_save, sender=MoodLog)
def update_streak(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        streak, _ = Streak.objects.get_or_create(user=user)

        # Update streak
        if streak.last_activity_date == date.today() - timedelta(days=1):
            streak.current_streak += 1
        else:
            streak.current_streak = 1

        streak.longest_streak = max(streak.longest_streak, streak.current_streak)
        streak.last_activity_date = date.today()
        streak.save()

        # Award badge
        if streak.current_streak == 7:
            Badge.objects.create(user=user, name="7-Day Streak", description="Logged mood for 7 consecutive days")
