from django.db import models
from users.models import User

class Badge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    awarded_at = models.DateTimeField(auto_now_add=True)