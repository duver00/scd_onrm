from django.shortcuts import render
from .models import Documento
from django.views.generic import  ListView


# Create your views here.
class DocumentosListView(ListView):
    template_name = 'data.html'
    context_object_name = 'doc_entradas'


    def get_queryset(self):
        return Documento.objects.all()


