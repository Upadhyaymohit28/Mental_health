from django.db import models
from users.models import User


class Badge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='badges')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    awarded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"


class Streak(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='streaks')
    current_streak = models.IntegerField(default=0)  # Days of consecutive activity
    longest_streak = models.IntegerField(default=0)  # Record of the longest streak
    last_activity_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.current_streak} days"


class DailyChallenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='daily_challenges')
    task = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    date_assigned = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.task} - {'Completed' if self.is_completed else 'Incomplete'}"


class ChallengeTemplate(models.Model):
    task = models.CharField(max_length=255)  # The challenge description
    difficulty = models.CharField(max_length=50, choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')],
                                  default='Easy')

    def __str__(self):
        return f"{self.task} ({self.difficulty})"
