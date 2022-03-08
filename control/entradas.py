from django.shortcuts import render, redirect
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .models import Documento
from django.views.generic import ListView, CreateView
from django.core.exceptions import ValidationError
from .forms import DocumentoForm
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
        data={}
        info={}
        try:
            if request.method == "POST":
                data = request.POST
                form = DocumentoForm()
                print(data)
                form.no_entrada_doc = data['no_entrada_doc']
                form.titulo = data['tiulo']
                form.f_entrada_doc = data['f_entrada_doc']
                form.dirigido = data['dirigido']
                form.organismo = data['organismo']
                form.entidad = data['entidad']
                form.t_documento = data['tipo_documento']
                form.observaciones = data['observaciones']
                if form.is_valid():
                    form.save()
                else:
                    info['error'] = 'Existe un error '
        except Exception as e:
            info['error'] = e
        return JsonResponse(data, safe='false')



























