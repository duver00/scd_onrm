from django.shortcuts import render


# Create your views here.

def DocumentosEntrada(request):
    return render(request, "data.html")
