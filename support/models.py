from django.db import models

class EmergencyContact(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    region = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} - {self.region}"

class ProfessionalConnection(models.Model):
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name