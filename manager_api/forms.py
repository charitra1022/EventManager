from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from .models import EventModel


class LoginForm(AuthenticationForm):
    username = UsernameField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Enter your username'}))

    password = forms.CharField(required=True, strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control mb-2 mt-1', 'placeholder': 'Enter your password'}))


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control mb-2 mt-1', 'placeholder': 'First Name'}))

    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control mb-2 mt-1', 'placeholder': 'Last Name'}))

    phone_number = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control mb-2 mt-1', 'placeholder': 'Phone Number'}))

    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control mb-2 mt-1', 'placeholder': 'Email'}))

    password1 = forms.CharField(required=True, label='Enter Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-2 mt-1', 'placeholder': 'New Password'}))

    password2 = forms.CharField(required=True, label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-2 mt-1', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'email': 'Email'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-2 mt-1', 'placeholder': 'Username'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False})

    def clean_first_name(self):
        # Capitalize first letter of first name
        first_name = self.cleaned_data.get('first_name', '')
        return first_name.capitalize()

    def clean_last_name(self):
        # Capitalize first letter of last name
        last_name = self.cleaned_data.get('last_name', '')
        return last_name.capitalize()

    def clean_username(self):
        # Make username field case-insensitive
        username = self.cleaned_data.get('username')
        return username.lower()


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ['title', 'description', 'start_date', 'end_date', 'registration_deadline', 'venue', 'registration_limit', 'banner']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Event Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Event Description'}),
            'start_date': DateTimeInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Event Start Time'}),
            'end_date': DateTimeInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Event End Time'}),
            'registration_deadline': DateTimeInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Registration Deadline'}),
            'venue': forms.TextInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Event Venue'}),
            'banner': forms.URLInput(attrs={'class': 'form-control mb-3 mt-1', 'placeholder': 'Event Banner URL'}),
            'registration_limit': forms.NumberInput(attrs={'class': 'form-control mb-3 mt-1', 'value':'-1', 'placeholder': 'Registration Limit'}),
        }

        labels = {
            'title': _('Event Title'),
            'description': _('Event Description'),
            'start_date': _('Event Start Time'),
            'end_date': _('Event End Time'),
            'venue': _('Event Venue'),
            'registration_deadline': _('Registration Deadline'),
            'banner': _('Event Poster Image URL'),
            'registration_limit': _('Registration Limit (-1 for unlimited registrations)'),
        }
