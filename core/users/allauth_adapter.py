from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

from .models import UserProfile

class CustomAccountAdapter(DefaultAccountAdapter):
     def save_user(self, request, user, form, commit=True):
          user = super().save_user(request, user, form, commit=False)
          
          user_profile = UserProfile(user=user)
          user_profile.save()

          return user
