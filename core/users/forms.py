from django.contrib.auth.models import User
from django import forms
from allauth.account.forms import LoginForm
from .models import UserProfile



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Change the class attribute of the form itself
        self.fields['login'].widget.attrs['class'] = 'form'
