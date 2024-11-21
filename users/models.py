from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    preferences = models.JSONField()  # Store chatbot preferences like tone
    mental_health_goals = models.TextField()