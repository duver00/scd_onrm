from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from control.models import Documento, Direcciones, Organismo, Entidad, TipoDocumento, Provincia
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from control.forms import DocumentoForm
from django.contrib.auth.mixins import LoginRequiredMixin

import datetime


# Create your views here.
class DocumentosListView(LoginRequiredMixin, ListView):
    template_name = 'entradas.html'
    context_object_name = 'list_entradas'
    login_url = '/entrar/'

    def get_queryset(self):
        return Documento.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_entradas'] = DocumentoForm()
        context['no_entrada'] = Documento.last_no_doc(Documento)
        return context


class NuevoDocumentoView(LoginRequiredMixin, CreateView):
    template_name = 'entradas.html'
    model = Documento
    form_class = DocumentoForm
    context_object_name = "list_entradas"
    login_url = '/entrar/'

    def post(self, request, *args, **kwargs):
        info = {}
        try:
            if request.method == 'POST':
                data = request.POST
                doc = Documento()
                org = Organismo()
                ent = Entidad()
                prov = Provincia()
                tdoc = TipoDocumento()
                dir = Direcciones()
                dir.pk = data['dirigido']
                ent.pk = data['entidad']
                org.pk = data['organismo']
                tdoc.pk = data['tipo_documento']
                prov.pk = data['provincia']
                doc.no_entrada_doc = data['no_entrada_doc']
                doc.titulo = request.POST['titulo']
                doc.f_entrada_doc = data['f_entrada_doc']
                doc.f_entrega_dirigido = data['f_dirigido']
                doc.f_termino = data['f_termino']
                doc.dirigido = dir
                doc.organismo = org
                doc.entidad = ent
                doc.t_documento = tdoc
                doc.provincia = prov
                doc.observaciones = data['observaciones']
                doc.soporte_doc = data['soporte']
                doc.forma_entrada = data['forma_entrada']
                doc.save()
                return JsonResponse(data)
            else:
                info['error'] = 'Existe un error '
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)


class EditarDocumento(LoginRequiredMixin, UpdateView):
    form_class = DocumentoForm
    model = Documento
    login_url = '/entrar/'

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


class EliminarDocumento(LoginRequiredMixin, DeleteView):
    model = Documento
    login_url = '/entrar/'

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






