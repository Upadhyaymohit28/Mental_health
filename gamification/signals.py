from datetime import date, timedelta
from moodtracking.models import MoodLog
from gamification.models import Badge, Streak
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from gamification.models import DailyChallenge, ChallengeTemplate
from django.contrib.auth.models import User
import random


@receiver(user_logged_in)
def generate_challenges_on_login(sender, request, user, **kwargs):
    """
    Generate daily challenges when a user logs in.
    """
    generate_challenges(user)


@receiver(post_save, sender=User)
def generate_challenges_on_signup(sender, instance, created, **kwargs):
    """
    Generate daily challenges when a new user signs up.
    """
    if created:
        generate_challenges(instance)


def generate_challenges(user):
    """
    Generate daily challenges for a user.
    """
    challenge_templates = ChallengeTemplate.objects.all()

    # Skip if a challenge already exists for today
    if DailyChallenge.objects.filter(user=user, date_assigned=date.today()).exists():
        return

    if challenge_templates.exists():
        # Randomly select a challenge template
        challenge_template = random.choice(challenge_templates)

        # Create a new challenge
        DailyChallenge.objects.create(
            user=user,
            task=challenge_template.task,
            date_assigned=date.today()
        )


@receiver(post_save, sender=MoodLog)
def update_streak(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        streak, _ = Streak.objects.get_or_create(user=user)

        # Check if the mood log is on the same day
        if streak.last_activity_date == date.today():
            # Do nothing if the user already logged today
            return

        # Update the streak
        if streak.last_activity_date == date.today() - timedelta(days=1):
            streak.current_streak += 1
        else:
            streak.current_streak = 1

        # Update the longest streak
        streak.longest_streak = max(streak.longest_streak, streak.current_streak)
        streak.last_activity_date = date.today()
        streak.save()

        # Award badges for streak milestones
        award_badges(user, streak.current_streak)


def award_badges(user, current_streak):
    """
    Award badges based on the user's current streak milestones, ensuring no duplicates.
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
            # Check if the badge already exists
            badge, created = Badge.objects.get_or_create(
                user=user,
                name=name,
                defaults={"description": description}
            )
            if created:
                # Log badge creation for debugging purposes
                print(f"Badge '{name}' awarded to user {user.username}")
