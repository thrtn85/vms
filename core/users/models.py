from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Permission


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    test = models.TextField()


class Role(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_choices = [
        ('VOLUNTEER', 'Volunteer'),
        ('ADMIN', 'Administrator'),
    ]
    role = models.CharField(max_length=20, choices=role_choices)

    def __str__(self):
        return self.role
