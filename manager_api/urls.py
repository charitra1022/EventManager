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
    path("my_events/", views.your_events, name="my_events")
]
