from django.shortcuts import render
from control.models import Documento, DocumentoSalida


# Create your views here.
def estadisticas_numeros(request):
    total = Documento.objects.count()
    print(total)
    return render(request, "inicio.html", {'total': total})
