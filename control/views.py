from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/entrar/')
def inicio(request):
    return render(request, "inicio.html")


def custom403(request, exception):
    return render(request, "403.html",{})


def custom404(request, exception):
    return render(request, "404.html",{})


def custom500(request):
    return render(request, "500.html",{})