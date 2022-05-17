from django.shortcuts import render


# Create your views here.

def registro(request):
    return render(request,"registro_entradas.html")
