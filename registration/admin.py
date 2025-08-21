from django.contrib import admin

# Register your models here.
# registration/admin.py

from django.contrib import admin
from .models import Event, Registration

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    list_filter = ('date', 'location')
    search_fields = ('title', 'description')

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'registration_date')
    list_filter = ('event', 'registration_date')
    search_fields = ('user__username', 'event__title')

admin.site.register(Event, EventAdmin)
admin.site.register(Registration, RegistrationAdmin)