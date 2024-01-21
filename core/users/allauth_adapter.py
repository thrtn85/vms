from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

from .models import UserProfile

class CustomAccountAdapter(DefaultAccountAdapter):
     def save_user(self, request, user, form, commit=True):
          user = super().save_user(request, user, form, commit=False)
          # Save the user first
          user.save()

          # Create and save the user profile
          user_profile = UserProfile(user=user)
          user_profile.save()

          return user