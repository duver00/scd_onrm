from django.shortcuts import get_object_or_404
from django.http import  JsonResponse
from control.models import Documento, Direcciones, Organismo, Entidad, TipoDocumento
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from control.forms import DocumentoForm

import datetime


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
    context_object_name = "list_entradas"

    def post(self, request, *args, **kwargs):
        info = {}
        try:
            if request.method == 'POST':
                data = request.POST
                doc = Documento()
                org = Organismo()
                ent = Entidad()
                tdoc = TipoDocumento()
                dir = Direcciones()
                dir.pk = data['dirigido']
                ent.pk = data['entidad']
                org.pk = data['organismo']
                tdoc.pk = data['tipo_documento']
                doc.no_entrada_doc = data['no_entrada_doc']
                doc.titulo = request.POST['titulo']
                doc.f_entrada_doc = data['f_entrada_doc']
                doc.dirigido = dir
                doc.organismo = org
                doc.entidad = ent
                doc.t_documento = tdoc
                doc.observaciones = data['observaciones']
                doc.save()
                return JsonResponse(data)
            else:
                info['error'] = 'Existe un error '
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)


class EditarDocumento(UpdateView):
    form_class = DocumentoForm
    model = Documento

    def post(self, request, *args, **kwargs):
        info = {}
        fn = {}
        agregado = {}
        try:
            if request.method == "POST":
                data = request.POST
                if len(data) == 2:
                    no_entrada = data['entrada']
                    if Documento.objects.get_or_create(no_entrada_doc=int(no_entrada)):
                        doc = Documento.objects.filter(no_entrada_doc=no_entrada)
                        for i in doc:
                            fn['pk'] = i.pk
                            fn['no_entrada_doc'] = i.no_entrada_doc
                            fn['titulo'] = i.titulo
                            fn['f_entrada'] = i.f_entrada_doc
                            fn['dirigido'] = i.dirigido.pk
                            fn['entidad'] = i.entidad.pk
                            fn['organismo'] = i.organismo.pk
                            fn['tipo_documento'] = i.t_documento.pk
                            fn['observaciones'] = i.observaciones
                    return JsonResponse(fn)
                elif len(data) > 2:
                    org = Organismo()
                    ent = Entidad()
                    tdoc = TipoDocumento()
                    dir = Direcciones()
                    dir.pk = data['dirigido']
                    ent.pk = data['entidad']
                    org.pk = data['organismo']
                    tdoc.pk = data['tipo_documento']
                    doc = Documento.objects.filter(no_entrada_doc=data['no_entrada_doc'])
                    for i in doc:
                        id_doc = i.pk
                    doc_editado = Documento.objects.get(pk=id_doc)
                    doc_editado.no_entrada_doc = data['no_entrada_doc']
                    doc_editado.f_entrada_doc = data['f_entrada_doc']
                    doc_editado.titulo = data['titulo']
                    doc_editado.dirigido = dir
                    doc_editado.organismo = org
                    doc_editado.entidad = ent
                    doc_editado.t_documento = tdoc
                    doc_editado.observaciones = data['observaciones']
                    doc_editado.save()
                    agregado['ok'] = 'editado'
                    return JsonResponse(agregado)
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)


class EliminarDocumento(DeleteView):
    model = Documento

    def post(self, request, *args, **kwargs):
        info = {}
        dat = {}
        try:
            if request.method == "POST":
                data = request.POST
                documento = Documento.objects.filter(no_entrada_doc=data['entrada'])
                for i in documento:
                    id_doc = i.pk
                    break
                doc = Documento.objects.get(pk=id_doc)
                dat['datos'] = doc
                doc.delete()
                return JsonResponse(dat)
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)






