from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .forms import AccountEditForm, UserProfileForm
from .models import UserProfile
from .tables import UserTable
from .utility import update_related_items


User = get_user_model()


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
def edit_account(request):
    if request.method == 'POST':
        user_form = AccountEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
        return redirect('/dashboard/') 
    else:
        user_form = AccountEditForm(instance=request.user)
    
    context = {
        'form': user_form,
    }
    return render(request, 'users/edit_account.html', context=context)


@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user  # Ensure the user is associated
            user_profile.save()
            
            # selected_interests = form.cleaned_data.get('interests', [])
            # update_related_items(user_profile, 'interests', selected_interests)

            # selected_skills = form.cleaned_data.get('skills', [])
            # update_related_items(user_profile, 'skills', selected_skills)

            return redirect('/dashboard/')  # Redirect to the dashboard
    else:
        form = UserProfileForm(instance=user_profile)

    context = {'form': form, 'created': created}

    return render(request, 'users/edit_profile.html', context)


@login_required
def user_mgmt(request):
    # list users (name, email, status, last activity, actions)
    
    table = UserTable(User.objects.all())
    table.paginate(page=request.GET.get("page", 1), per_page=25)

    context = {
        "heading": "User Management",
        "table": table
    }
    return render(request, 'users/user_mgmt.html', context=context)