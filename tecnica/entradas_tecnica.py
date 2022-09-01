from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import DocumentosTecnica
from .forms import DocumentoTecnicaForm
from control.models import TipoDocumento,Direcciones,Entidad,Organismo,Provincia
from django.http import JsonResponse
from django.views.defaults import ERROR_403_TEMPLATE_NAME


class DocumentosTecnicaView(LoginRequiredMixin,PermissionRequiredMixin, TemplateView):
    template_name = "tecnica_entradas.html"
    permission_required = 'tecnica.view_documentostecnica'
    login_url = "/entrar/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_entradas'] = DocumentoTecnicaForm()
        context['no_tecnica'] = DocumentosTecnica.objects.all().last()
        context['list_tipos_documentos'] = TipoDocumento.objects.all()
        context['list_organismos'] = Organismo.objects.all()
        context['list_direcciones'] = Direcciones.objects.all()
        context['list_provincias'] = Provincia.objects.all()
        context['list_entidad'] = Entidad.objects.all()
        context['list_entradas'] = DocumentosTecnica.objects.all()
        return context



class NuevoDocumentoTecnicaView(LoginRequiredMixin, CreateView):
    template_name = "tecnica_entradas.html"
    form_class = DocumentoTecnicaForm
    model = DocumentosTecnica
    permission_required = 'tecnica.add_documentostecnica'
    login_url = '/entrar/'


    def post(self, request, *args, **kwargs):
        info = {}
        try:
            if request.method == 'POST':
                data = request.POST
                doc = DocumentosTecnica()
                org = Organismo()
                print('dadad')
                ent = Entidad()
                prov = Provincia()
                tdoc = TipoDocumento()
                ent.pk = data['entidad']
                org.pk = data['organismo']
                tdoc.pk = data['tipo_documento']
                prov.pk = data['provincia']
                doc.no_entrada = data['no_entrada_doc']
                doc.no_tecnica = data['no_tecnica_doc']
                doc.titulo = ['titulo']
                doc.f_entrada_tecnica = data['f_entrada_tecnica']
                doc.organismo = org
                doc.entidad = ent
                doc.t_documento = tdoc
                doc.provincia = prov
                doc.observaciones = data['observaciones']
                doc.save()
                return JsonResponse(data)
            else:
                info['error'] = 'Existe un error '
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)


class EditarDocumentoTecnicaView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    template_name = "tecnica_entradas.html"
    form_class = DocumentoTecnicaForm
    model = DocumentosTecnica
    permission_required = 'tecnica.change_documentostecnica'
    login_url = '/entrar/'

    def post(self, request, *args, **kwargs):
        info = {}
        fn = {}
        agregado = {}
        try:
            if request.method == "POST":
                data = request.POST
                if len(data) == 2:
                    if DocumentosTecnica.objects.get_or_create(no_tecnica=data['tecnica']):
                        doc = DocumentosTecnica.objects.filter(no_tecnica=data['tecnica'])
                        for i in doc:
                            fn['pk'] = i.pk
                            fn['no_entrada_doc'] = i.no_entrada
                            fn['no_tecnica'] = i.no_tecnica
                            fn['titulo'] = i.titulo
                            fn['f_entrada_tecnica'] = i.f_entrada_tecnica
                            fn['entidad'] = i.entidad.pk
                            fn['organismo'] = i.organismo.pk
                            fn['tipo_documento'] = i.t_documento.pk
                            fn['observaciones'] = i.observaciones
                            fn['provincia'] = i.provincia.pk
                    return JsonResponse(fn)
                elif len(data) > 2:
                    org = Organismo()
                    ent = Entidad()
                    tdoc = TipoDocumento()
                    prov = Provincia()
                    ent.pk = data['entidad']
                    org.pk = data['organismo']
                    tdoc.pk = data['tipo_documento']
                    prov.pk = data['provincia']
                    doc = DocumentosTecnica.objects.filter(no_tecnica=data['no_tecnica_entrada'])
                    for i in doc:
                        id_doc = i.pk
                        break
                    doc_editado = DocumentosTecnica.objects.get(pk=id_doc)
                    doc_editado.no_entrada = data['no_entrada_doc']
                    doc_editado.no_tecnica = data['no_tecnica_entrada']
                    doc_editado.f_entrada_tecnica = data['f_entrada_tecnica']
                    doc_editado.titulo = data['titulo']
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


class EliminarDocumentoTecnicaView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = DocumentosTecnica
    permission_required = 'tecnica.delete_documentostecnica'
    login_url = '/entrar/'

    def post(self, request, *args, **kwargs):
        info = {}
        dat = {}
        try:
            if request.method == "POST":
                data = request.POST
                documento = DocumentosTecnica.objects.filter(no_tecnica=data['tecnica'])
                for i in documento:
                    id_doc_tec = i.pk
                    break
                doc = DocumentosTecnica.objects.get(pk=id_doc_tec)
                dat['datos'] = 'Documento Eliminado'
                doc.delete()
                return JsonResponse(dat)
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)

