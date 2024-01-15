from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
#from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialApp, SocialAccount
#from allauth.socialaccount.admin import SocialAppAdmin

admin.site.unregister(SocialApp)
admin.site.unregister(SocialAccount)


class ProfileInline(admin.StackedInline):
     model = UserProfile
     can_delete = False
     verbose_name_plural = 'Manage Profile'


class CustomUserAdmin(admin.ModelAdmin):
     list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')
     list_filter = ('is_active', 'date_joined',)
     search_fields = ('username', 'email', 'first_name', 'last_name')
     readonly_fields = ('last_login',)
     inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)



