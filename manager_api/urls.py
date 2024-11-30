from django.urls import include, path
from django.contrib.auth import views as auth_views

from . import views
from . import forms

urlpatterns = [
    path('', views.homepage, name="homepage"),

    # path('registration/', views.CustomerRegistrationView.as_view(),
    #      name='customerregistration'),
    path('login/', auth_views.LoginView.as_view(template_name='manager_api/login.html', authentication_form=forms.LoginForm, next_page='/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path("register/", views.registerPage, name="register"),
    path("login_user/", views.loginUser, name="login_user"),
    path("register_user/", views.registerUser, name="register_user"),
]
