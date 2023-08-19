from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import UserProfile
from django.contrib.auth.forms import PasswordResetForm



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
