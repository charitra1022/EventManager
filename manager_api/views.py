from django.shortcuts import render, redirect


def homepage(req):
    return render(req, "manager_api/home.html")

def loginPage(req):
    return render(req, "manager_api/login.html")

def loginUser(req):
    return redirect("login")

def registerPage(req):
    return render(req, "manager_api/register.html")

def registerUser(req):
    return redirect("register")

