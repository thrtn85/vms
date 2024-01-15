from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import UserProfile



class AccountEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user',]
        # widgets = {
        #     'skills': forms.CheckboxSelectMultiple(attrs={'class': 'list-unstyled'}),
        #     'interests': forms.CheckboxSelectMultiple(attrs={'class': 'list-unstyled'}),
        # }