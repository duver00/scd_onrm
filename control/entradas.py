from django.http import JsonResponse
from control.models import Documento, Direcciones, Organismo, Entidad, TipoDocumento, Provincia
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from control.forms import DocumentoForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


import datetime


# Create your views here.
class DocumentosTemplateView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = "entradas.html"
    permission_required = 'control.view_documento'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_entradas'] = DocumentoForm()
        context['no_entrada'] = Documento.objects.all().last()
        context['list_tipos_documentos'] = TipoDocumento.objects.all()
        context['list_organismos'] = Organismo.objects.all()
        context['list_direcciones'] = Direcciones.objects.all()
        context['list_provincias'] = Provincia.objects.all()
        context['list_entidad'] = Entidad.objects.all()
        context['list_formas_entrada'] = Documento.Entrada
        context['list_entradas'] = Documento.objects.all()
        return context


class NuevoDocumentoView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    template_name = 'entradas.html'
    model = Documento
    form_class = DocumentoForm
    context_object_name = "list_entradas"
    permission_required = 'control.add_documento'
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
            else:
                info['error'] = 'Existe un error '
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)


class EditarDocumento(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    form_class = DocumentoForm
    model = Documento
    permission_required = 'control.change_documento'
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
                            fn['entidad'] = i.entidad.pks
                            fn['organismo'] = i.organismo.pk
                            fn['tipo_documento'] = i.t_documento.pk
                            fn['observaciones'] = i.observaciones
                            fn['f_entrada_doc'] = i.forma_entrada
                            fn['soporte_doc'] = i.soporte_doc
                            fn['provincia'] = i.provincia.pk
                            fn['f_termino'] = i.f_termino
                            fn['f_dirigido'] = i.f_entrega_dirigido
                    return JsonResponse(fn)
                elif len(data) > 2:
                    org = Organismo()
                    ent = Entidad()
                    tdoc = TipoDocumento()
                    dir = Direcciones()
                    prov = Provincia()
                    dir.pk = data['dirigido']
                    ent.pk = data['entidad']
                    org.pk = data['organismo']
                    tdoc.pk = data['tipo_documento']
                    prov.pk = data['provincia']
                    doc = Documento.objects.filter(no_entrada_doc=data['no_entrada_doc'])
                    for i in doc:
                        id_doc = i.pk
                    doc_editado = Documento.objects.get(pk=id_doc)
                    doc_editado.no_entrada_doc = data['no_entrada_doc']
                    doc_editado.f_entrada_doc = data['f_entrada_doc']
                    doc_editado.titulo = data['titulo']
                    doc_editado.f_termino = data['f_termino']
                    doc_editado.soporte_doc = data['soporte_doc']
                    doc_editado.forma_entrada = data['forma_entrada']
                    doc_editado.f_entrega_dirigido = data['f_dirigido']
                    doc_editado.dirigido = dir
                    doc_editado.organismo = org
                    doc_editado.entidad = ent
                    doc_editado.t_documento = tdoc
                    doc_editado.provincia = prov
                    doc_editado.observaciones = data['observaciones']
                    doc_editado.save()
                    agregado['ok'] = 'editado'
                    return JsonResponse(agregado)
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)


class EliminarDocumento(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Documento
    permission_required = 'control.delete_documento'
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






