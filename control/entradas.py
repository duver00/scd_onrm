from django.shortcuts import render, redirect
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .models import Documento
from django.views.generic import ListView, CreateView
from django.core.exceptions import ValidationError
from .forms import DocumentoForm


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
        form = DocumentoForm(request.POST)
        data={}
        if form.is_valid():
            form.save()
            data['status'] = "ok"
            return JsonResponse()
        else:
            data['error'] = form.errors
            return JsonResponse(data, safe=False)

















