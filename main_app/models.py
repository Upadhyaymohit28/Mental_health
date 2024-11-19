from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.IntegerField()  # Scale from 1 to 10
    note = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mood} on {self.date.strftime('%Y-%m-%d')}"
    def get_points(self):
        return self.mood  # Simple example: mood score equals points