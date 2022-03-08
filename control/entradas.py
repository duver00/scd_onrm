from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from control.models import Documento, Direcciones
from django.views.generic import ListView, CreateView
from django.core.exceptions import ValidationError
from control.forms import DocumentoForm
import json


# Create your views here.
class DocumentosListView(ListView):
    template_name = 'data.html'
    context_object_name = 'list_entradas'

    def get_queryset(self):
        return Documento.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_entradas'] = DocumentoForm()
        context['no_entrada'] = Documento.last_no_doc(Documento)
        return context


class NuevoDocumentoView(CreateView):
    template_name = 'data.html'
    model = Documento
    form_class = DocumentoForm
    success_url = '/entradas/'
    context_object_name = "list_entradas"

    def post(self, request, *args, **kwargs):
        data = {}
        info = {}
        try:
            if request.method == "POST":
                data = request.POST
                doc = Documento()
                dir = Direcciones()
                doc.no_entrada_doc = data['no_entrada_doc']
                doc.titulo = request.POST['titulo']
                doc.f_entrada_doc = data['f_entrada_doc']
                doc.dirigido = data['dirigido']
                doc.organismo.nombre = data['organismo']
                doc.entidad.nombre = data['entidad']
                doc.t_documento.tipo = data['tipo_documento']
                doc.observaciones = data['observaciones']
                doc.save()
                return JsonResponse(data)
            else:
                info['error'] = 'Existe un error '
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)
