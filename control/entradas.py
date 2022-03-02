from django.shortcuts import render
from .models import Documento
from django.views.generic import ListView
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
        return context



