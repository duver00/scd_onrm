from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class LoginScd(LoginView):
    template_name = "login.html"


class LogoutSCD(LoginRequiredMixin, LogoutView):
    pass

