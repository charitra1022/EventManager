from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone

from .forms import RegistrationForm, EventCreationForm
from .models import UserModel, EventModel

from .enums import EventOccurence

def compare_datetime(starttime, endtime, deadline):
    """
    Give the state of the event

    Parameters
        starttime -> Django DateTimeField value for start time
        endtime -> Django DateTimeField value for end time
        deadline -> Django DateTimeField value for registration deadline time

    Returns: A tuple that can contain any of the combination of below enum values
        EventOccurence.PAST -> if the event was in past
        EventOccurence.ONGOING -> if the event is currently ongoing
        EventOccurence.UPCOMING -> if the event is upcoming
        EventOccurence.CLOSED -> if the event registration is closed
        EventOccurence.OPEN -> if the event registration is open
    """
    now = timezone.now()
    registration = EventOccurence.CLOSED if deadline <= now else EventOccurence.OPEN
    if starttime > now:
        return EventOccurence.UPCOMING, registration
    elif endtime <= now:
        return EventOccurence.PAST, registration
    elif starttime <= now < endtime:
        return EventOccurence.ONGOING, registration


def homepage(req):
    context = {}

    past_events = []
    ongoing_events = []
    upcoming_events = []
    registered_events = []

    events = EventModel.objects.all()

    for event in events:
        event_occ = compare_datetime(event.start_date, event.end_date, event.registration_deadline)
        if EventOccurence.PAST in event_occ:
            past_events.append(event)
        if EventOccurence.UPCOMING in event_occ:
            upcoming_events.append(event)
        if EventOccurence.ONGOING in event_occ:
            ongoing_events.append(event)

    context['past_events'] = past_events
    context['ongoing_events'] = ongoing_events
    context['upcoming_events'] = upcoming_events
    context['registered_events'] = registered_events


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
            form = RegistrationForm()
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
    profile = UserModel.objects.get(user=User.objects.get(username=req.user.username))
    if not profile.is_organizer: return redirect("dashboard")

    events = EventModel.objects.filter(organizer=profile)
    context["events"] = events

    return render(req, "manager_api/organizer_events.html", context)


class Create_Event_View(LoginRequiredMixin, View):
    login_url = "/login/"
    redirect_field_name = "next"

    def get(self, req):
        context = {}
        profile = UserModel.objects.get(user=User.objects.get(username=req.user.username))
        if not profile.is_organizer: return redirect("dashboard")

        form = EventCreationForm()
        return render(req, "manager_api/create_event.html", {"form": form})

    def post(self, req):
        context = {}
        profile = UserModel.objects.get(user=User.objects.get(username=req.user.username))
        if not profile.is_organizer: return redirect("dashboard")

        form = EventCreationForm(req.POST)
        if form.is_valid():
            messages.success(req, 'Event created Successfully!')
            ev_id = form.save()
            EventModel.objects.filter(pk=ev_id.id).update(organizer=profile)
            form = EventCreationForm()
        return render(req, 'manager_api/create_event.html', {'form': form})


def event_details(req, pk):
    context = {}
    try:
        event = EventModel.objects.get(id=pk)
        context['event'] = event
        event_occ = compare_datetime(event.start_date, event.end_date, event.registration_deadline)
        context['registration_closed'] = True if EventOccurence.CLOSED in event_occ else False
        return render(req, "manager_api/event_details.html", context)

    except Exception as ex:
        return render(req, "manager_api/404.html")
