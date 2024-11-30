from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import RegistrationForm
from .models import UserModel


def homepage(req):
    context = {}
    return render(req, "manager_api/home.html", context)


class RegistrationView(View):
    # for register page
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'manager_api/register.html', {'form': form})

    # for submission of form
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created Successfully!')
            form.save()
            phn = form.cleaned_data['phone_number']
            user = User.objects.get(username=form.clean_username())
            UserModel(phone_number=phn, user=user).save()
        return render(request, 'manager_api/register.html', {'form': form})


@login_required(login_url="/login/")
def user_dashboard(req):
    context = {}
    if req.user.is_authenticated:
        profile = UserModel.objects.get(user=User.objects.get(username=req.user.username))
        context['profile'] = profile
    return render(req, "manager_api/dashboard.html", context)


@login_required(login_url="/login/")
def your_events(req):
    context = {}
    return render(req, "manager_api/organizer_events.html", context)
