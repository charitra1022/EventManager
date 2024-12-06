from tkinter.font import names

from django.urls import include, path
from django.contrib.auth import views as auth_views

from . import views
from . import forms

urlpatterns = [
    path('', views.homepage, name="homepage"),

    path('login/', auth_views.LoginView.as_view(template_name='manager_api/login.html', authentication_form=forms.LoginForm, next_page='/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='homepage'), name='logout'),
    path("register/", views.RegistrationView.as_view(), name="register"),

    path("dashboard/", views.user_dashboard, name="dashboard"),
    path("my_events/", views.your_events, name="my_events"),

    path("create_event/", views.Create_Event_View.as_view(), name="create_event"),

    path("event/<int:pk>/", views.event_details, name="event_details")
]
