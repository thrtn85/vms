from django.contrib.auth.models import User
from django import forms
from .models import UserProfile



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

