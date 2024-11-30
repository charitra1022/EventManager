from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))

    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control password-field', 'placeholder': 'Enter your password'}))


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control mt-2', 'placeholder': 'First Name'}))

    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control mt-2', 'placeholder': 'Last Name'}))

    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control mt-2', 'placeholder': 'New Password'}))

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control mt-2', 'placeholder': 'Confirm Password'}))

    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control mt-2', 'placeholder': 'Email'}))

    phone_number = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control mt-2', 'placeholder': 'Phone Number'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
        labels = {
            'email': 'Email'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Username'}),
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