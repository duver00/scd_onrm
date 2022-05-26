from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView, CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import TipoDocumentoSalida, DocumentoSalida, Organismo, Entidad, Provincia, Direcciones
from .forms import DocumentoSalidaForm


class DocumentoSalidaTemplateView(LoginRequiredMixin,PermissionRequiredMixin, TemplateView):
    template_name = "salidas.html"
    permission_required = 'control.view_documentosalida'
    login_url = '/entrar/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_salidas'] = DocumentoSalida.objects.all()
        context['form_salidas'] = DocumentoSalidaForm()
        context['list_organismos'] = Organismo.objects.all()
        context['list_tipos_documentos_salidas'] = TipoDocumentoSalida.objects.all()
        context['list_direcciones'] = Direcciones.objects.all()
        context['list_provincias'] = Provincia.objects.all()
        context['list_entidad'] = Entidad.objects.all()
        context['list_formas_salidas'] = DocumentoSalida.Salida
        context['no_salida'] = DocumentoSalida.objects.all().last()
        return context


class NuevoDocumentoSalidaView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    template_name = 'salidas.html'
    model = DocumentoSalida
    form_class = DocumentoSalidaForm
    permission_required = 'control.add_documentossalida'
    login_url = '/entrar/'

    def post(self, request, *args, **kwargs):
        info = {}
        try:
            if request.method == 'POST':
                data = request.POST
                doc = DocumentoSalida()
                orga = Organismo()
                ent = Entidad()
                prov = Provincia()
                tdoc = TipoDocumentoSalida()
                dir = Direcciones()
                dir.pk = data['procedencia']
                ent.pk = data['entidad']
                orga.pk = data['organismo']
                tdoc.pk = data['tipo_documento_salida']
                prov.pk = data['provincia']
                doc.no_salida_doc = data['no_salida_doc']
                doc.titulo = data['titulo']
                doc.f_salida_doc = data['f_salida_doc']
                doc.organismo = orga
                doc.entidad = ent
                doc.t_documento_salida = tdoc
                doc.provincia = prov
                doc.procedencia = dir
                doc.observaciones = data['observaciones']
                doc.soporte_doc_salida = data['soporte_salida']
                doc.forma_salida = data['forma_salida']
                doc.save()
                return JsonResponse(data)
            else:
                info['error'] = 'Existe un error '
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)


class EditarDocumentoSalidasView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    form_class = DocumentoSalidaForm
    model = DocumentoSalida
    permission_required = 'control.change_documentossalida'
    login_url = '/entrar/'

    def post(self, request, *args, **kwargs):
        info = {}
        fn = {}
        agregado = {}
        try:
            if request.method == "POST":
                data = request.POST
                if len(data) == 2:
                    no_salida = data['salida']
                    if DocumentoSalida.objects.get_or_create(no_salida_doc=int(no_salida)):
                        doc = DocumentoSalida.objects.filter(no_salida_doc=no_salida)
                        for i in doc:
                            fn['pk'] = i.pk
                            fn['no_salida_doc'] = i.no_salida_doc
                            fn['titulo'] = i.titulo
                            fn['f_salida_doc'] = i.f_salida_doc
                            fn['procedencia'] = i.procedencia.pk
                            fn['entidad'] = i.entidad.pk
                            fn['organismo'] = i.organismo.pk
                            fn['tipo_documento_salida'] = i.t_documento_salida.pk
                            fn['observaciones'] = i.observaciones
                            fn['forma_salida'] = i.forma_salida
                            fn['soporte_salida'] = i.soporte_doc_salida
                            fn['provincia'] = i.provincia.pk
                    return JsonResponse(fn)
                elif len(data) > 2:
                    org = Organismo()
                    ent = Entidad()
                    tdoc = TipoDocumentoSalida()
                    dir = Direcciones()
                    prov = Provincia()
                    dir.pk = data['procedencia']
                    ent.pk = data['entidad']
                    org.pk = data['organismo']
                    tdoc.pk = data['tipo_documento_salida']
                    prov.pk = data['provincia']
                    doc = DocumentoSalida.objects.filter(no_salida_doc=data['no_salida_doc'])
                    for salida in doc:
                        id_doc = salida.pk
                    doc_editado = DocumentoSalida.objects.get(pk=id_doc)
                    doc_editado.no_salida_doc = data['no_salida_doc']
                    doc_editado.f_salida_doc = data['f_salida_doc']
                    doc_editado.titulo = data['titulo']
                    doc_editado.soporte_doc = data['soporte_salida']
                    doc_editado.forma_salida = data['forma_salida']
                    doc_editado.procedencia = dir
                    doc_editado.organismo = org
                    doc_editado.entidad = ent
                    doc_editado.t_documento_salida = tdoc
                    doc_editado.provincia = prov
                    doc_editado.soporte_doc_salida = data['soporte_salida']
                    doc_editado.observaciones = data['observaciones']
                    doc_editado.save()
                    agregado['ok'] = 'editado'
                    return JsonResponse(agregado)
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)



class EliminarDocumentoSalidasView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = DocumentoSalida
    permission_required = 'control.delete_documentossalida'
    login_url = '/entrar/'

    def post(self, request, *args, **kwargs):
        info = {}
        dat = {}
        try:
            if request.method == "POST":
                data = request.POST
                documento = DocumentoSalida.objects.filter(no_salida_doc=data['salida'])
                for i in documento:
                    id_doc = i.pk
                    break
                doc = DocumentoSalida.objects.get(pk=id_doc)
                dat['datos'] = doc
                doc.delete()
                return JsonResponse(dat)
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)




