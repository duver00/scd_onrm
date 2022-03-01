from django.shortcuts import render
from .models import Documento


# Create your views here.

def DocumentosEntrada(request):
    doc_entradas = Documento.objects.all()
    return render(request, "data.html", {"doc_entradas": doc_entradas})
