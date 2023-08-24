from django.contrib import admin
from django.contrib.auth.models import User
from .models import Role
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialApp
#from allauth.socialaccount.admin import SocialAppAdmin

admin.site.unregister(EmailAddress)  # Optional if you don't need to manage email addresses
admin.site.unregister(SocialApp)
#admin.site.unregister(SocialAppAdmin)


class RoleInline(admin.StackedInline):
     model = Role
     can_delete = False
     verbose_name_plural = 'Role'


class CustomUserAdmin(admin.ModelAdmin):
     list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'is_active')
     list_filter = ('is_active', 'date_joined')
     search_fields = ('username', 'email', 'first_name', 'last_name')
     inlines = [RoleInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


