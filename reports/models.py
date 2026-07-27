from django.db import models
from django.contrib.auth.models import User

class Incident(models.Model):
    SEVERITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incidents')
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default='LOW')
    location_name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    photo = models.ImageField(upload_to='incidents/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.severity})"


class StreetLight(models.Model):
    CONDITION_CHOICES = [
        ('WORKING', 'Working'),
        ('DIM', 'Dim / Flickering'),
        ('BROKEN', 'Out / Broken'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='streetlights')
    location_name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='BROKEN')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Light at {self.location_name} - {self.get_condition_display()}"


class CrowdReport(models.Model):
    DENSITY_CHOICES = [
        ('LOW', 'Low / Deserted'),
        ('MEDIUM', 'Moderate Crowd'),
        ('HIGH', 'Heavy Crowd'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='crowd_reports')
    location_name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    density = models.CharField(max_length=20, choices=DENSITY_CHOICES, default='MEDIUM')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Crowd at {self.location_name} - {self.get_density_display()}"