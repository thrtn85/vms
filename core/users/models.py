from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Permission


class Skills(models.Model):
    name = models.TextField(verbose_name="Skill Name")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Skills"

class Interests(models.Model):
    name = models.TextField(verbose_name="Interest Name")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Interests"

class UserProfile(models.Model):
    LOCATION = [
        ('remote','Remote'),
        ('on-site','On-Site')
    ]

    # Personal Information
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(verbose_name="Date of Birth", blank=True, null=True)
    
    # Profile Picture
    profile_img = models.FileField(upload_to='profile_images/')

    # Skills and Interests
    skills = models.ManyToManyField('Skills', blank=True)
    interests = models.ManyToManyField('Interests', blank=True)

    # Availability
    # Experience
    # Bio or Introduction
    bio = models.TextField(blank=True, null=True)

    # Preferred Volunteer Opportunities
    # --- this should come from opportunities model

    # Location Preference
    location = models.CharField(verbose_name="Location Preference", max_length = 20, choices=LOCATION)

    # References
    # Emergency Contact Information

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = "User Profiles"

class Role(models.Model):
    role_choices = [
        ('VOLUNTEER', 'Volunteer'),
        ('ADMIN', 'Administrator'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=role_choices)

    def __str__(self):
        return self.role
