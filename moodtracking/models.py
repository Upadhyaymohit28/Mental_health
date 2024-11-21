from django.db import models
from users.models import User


class MoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood_score = models.IntegerField()
    sentiment_analysis_result = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.age} - {self.mood_score} on {self.date.strftime('%Y-%m-%d')}"

    def get_points(self):
        return self.mood_score  # Simple example: mood score equals points
