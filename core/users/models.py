from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class UserProfile(models.Model):
    ROLES = [
        ('NONE', 'None'),
        ('MANAGER', 'Program Manager'),
        ('ADMIN', 'Administrator'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLES, default='NONE')

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = "User Profiles"