from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import User
from django.db.models import ForeignKey


class UserModel(models.Model):
    # firstName, lastName, email, username, password --> already present in USER
    phone_number = models.BigIntegerField(blank=True)
    is_organizer = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.first_name + " " + self.user.email


class EventModel(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    venue = models.CharField(max_length=100, null=True)
    registration_deadline = models.DateTimeField(null=True)
    banner = models.TextField(validators=[URLValidator()], null=True)
    organizer = models.ForeignKey(
        UserModel, on_delete=models.SET_NULL, null=True)
    registration_limit = models.IntegerField(default=-1)    # -1 means no limit on registrations

    def __str__(self) -> str:
        return f"\"{self.title}\" by {self.organizer.user.username}"


class RegistrationsModel(models.Model):
    event = ForeignKey(EventModel, on_delete=models.CASCADE)
    attendee = ForeignKey(UserModel, on_delete=models.CASCADE)
    registration_time = models.DateTimeField(null=True)

