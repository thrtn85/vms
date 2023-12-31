from django.urls import reverse_lazy
from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from allauth.account.views import LoginView
from .forms import UserEditForm




def home(request):
    user = request.user # get current logged in user

    context = {
        "welcome": "Welcome",
        "user": user
    }
    return render(request, 'home.html', context)

@login_required
def dashboard(request):


    context = {
        "welcome": "Welcome to your dashboard"
    }
    return render(request, 'users/dashboard.html', context=context)

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'users/edit_profile.html', context=context)




