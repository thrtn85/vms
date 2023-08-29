from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
#from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialApp, SocialAccount
#from allauth.socialaccount.admin import SocialAppAdmin

admin.site.unregister(SocialApp)
admin.site.unregister(SocialAccount)
admin.site.register(Skills)
admin.site.register(Interests)

class RoleInline(admin.StackedInline):
     model = Role
     can_delete = False
     verbose_name_plural = 'Role'

class ProfileInline(admin.StackedInline):
     model = UserProfile
     can_delete = False
     verbose_name_plural = 'User Profile'


class CustomUserAdmin(admin.ModelAdmin):
     list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_active')
     list_filter = ('is_active', 'date_joined', 'role')
     search_fields = ('username', 'email', 'first_name', 'last_name')
     readonly_fields = ('last_login','password')
     inlines = [RoleInline, ProfileInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class UserProfileAdmin(admin.ModelAdmin):
     list_display = ('user', 'location',)
     list_filter = ('location',)
     search_fields = ('user__username',)
     # List of fields to make read-only
     readonly_fields = ('user',)
     # inlines = []

#admin.site.register(UserProfile, UserProfileAdmin)
