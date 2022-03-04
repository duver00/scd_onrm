from django.shortcuts import render, redirect
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .models import Documento
from django.views.generic import ListView, CreateView
from django.core.exceptions import ValidationError
from .forms import DocumentoForm
from django.forms import model_to_dict


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
        if request.method == "POST":
            form = DocumentoForm(request.POST)
            if form.is_valid():
                form.save()
                instance = form
                return JsonResponse(model_to_dict(instance, fields=['titulo']), status=201)
            else:
                return JsonResponse(form.errors, safe=False)
        return render(request, "data.html")


















