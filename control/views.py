from django.shortcuts import render
from .models import DocumentoSalida, Documento
from tecnica.models import DocumentosTecnica, SalidasTecnica
from registro.models import DocumentosRegistro, SalidasRegistro
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.
@login_required(login_url='/entrar/')
def inicio(request):
    total = DocumentoSalida.objects.all().count() + Documento.objects.all().count()
    total_entradas = Documento.objects.all().count()
    total_salidas = DocumentoSalida.objects.all().count()
    anno_curso = Documento.objects.filter(f_entrada_doc__year=datetime.date.today().year).count() + \
                 DocumentoSalida.objects.filter(f_salida_doc__year=datetime.date.today().year).count()
    total_tec_entradas = DocumentosTecnica.objects.all().count()
    total_tec_salidas = SalidasTecnica.objects.all().count()
    total_reg_salidas = SalidasRegistro.objects.all().count()
    total_reg_entradas = DocumentosRegistro.objects.all().count()
    return render(request, "inicio.html",{'total':total, 'total_entradas':total_entradas,'total_salidas':total_salidas,
                                          'anno_curso':anno_curso, 'total_tec_entradas':total_tec_entradas,
                                          'total_tec_salidas':total_tec_salidas, 'total_reg_salidas':total_reg_salidas,
                                          'total_reg_entradas':total_reg_entradas})


def custom403(request, exception):
    return render(request, "403.html",{})


def custom404(request, exception):
    return render(request, "404.html",{})


def custom500(request):
    return render(request, "500.html",{})