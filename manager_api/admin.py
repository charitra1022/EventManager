from django.contrib import admin
from .models import UserModel, EventModel, RegistrationsModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'name', 'email', 'phone_number', 'is_organizer']

    def username(self, obj):
        return obj.user.username

    def name(self, obj):
        full_name = (obj.user.first_name + " " + obj.user.last_name).strip()
        if len(full_name) == 0: return "-"
        return full_name

    def email(self, obj):
        return obj.user.email


@admin.register(EventModel)
class EventModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_date', 'end_date', 'venue', 'registration_deadline', 'organizer', 'limit', 'banner']

    def limit(self, obj):
        return obj.registration_limit


@admin.register(RegistrationsModel)
class RegistrationsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'attendee', 'registration_time']
