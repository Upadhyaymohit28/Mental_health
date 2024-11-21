from django.db import models
from users.models import User


class MoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mood_logs')
    mood_score = models.IntegerField()  # Scale: 1 (low) to 10 (high)
    description = models.TextField(blank=True)  # Optional text entry for mood
    sentiment = models.CharField(max_length=50, blank=True)  # Result from AI analysis
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mood_score} - {self.timestamp}"

    def get_points(self):
        return self.mood_score  # Simple example: mood score equals points
