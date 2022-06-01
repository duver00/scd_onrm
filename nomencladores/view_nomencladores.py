from nomencladores.forms import DireccionesForm
from django.shortcuts import render


def direcciones(request):
    return render(request,"modals/direcciones.html",{'form_direcciones': DireccionesForm()})