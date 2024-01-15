from django.contrib import admin
from .models import *


class VolunteerAdmin(admin.ModelAdmin):
     list_display = ('photo','name', )
     #list_filter = ('',)
     search_fields = ('name',)
     # List of fields to make read-only
     #readonly_fields = ('',)

admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Skills)
admin.site.register(Interests)