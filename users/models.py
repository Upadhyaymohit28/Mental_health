from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.IntegerField(null=True, blank=True)
    preferences = models.JSONField(default=dict, blank=True)
    mental_health_goals = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Notification(models.Model):
    TYPE_CHOICES = [
        ('message', 'Message'),
        ('reminder', 'Reminder'),
        ('alert', 'Alert'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    url = models.URLField(max_length=500, blank=True)
    is_unread = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title