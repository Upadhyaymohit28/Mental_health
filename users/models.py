from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.IntegerField(null=True, blank=True)
    preferences = models.JSONField(default=dict, blank=True)
    mental_health_goals = models.TextField(blank=True)

    def __str__(self):
        return self.user.username