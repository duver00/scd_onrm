from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import DocumentosRegistro
from .forms import DocumentoRegistroForm
from control.models import TipoDocumento,Direcciones,Entidad,Organismo,Provincia
from django.http import JsonResponse



class DocumentoRegistroView(LoginRequiredMixin, TemplateView):
    template_name = "registro_entradas.html"
    login_url = "/entrar/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_entradas'] = DocumentoRegistroForm()
        context['no_registro'] = DocumentosRegistro.objects.all().last()
        context['list_tipos_documentos'] = TipoDocumento.objects.all()
        context['list_organismos'] = Organismo.objects.all()
        context['list_direcciones'] = Direcciones.objects.all()
        context['list_provincias'] = Provincia.objects.all()
        context['list_entidad'] = Entidad.objects.all()
        context['list_entradas'] = DocumentosRegistro.objects.all()
        return context


class NuevoDocumentoRegistroView(LoginRequiredMixin, CreateView ):
    template_name = "registro_entradas.html"
    form_class = DocumentoRegistroForm
    model = DocumentosRegistro
    login_url = '/entrar/'


    def post(self, request, *args, **kwargs):
        info = {}
        try:
            if request.method == 'POST':
                data = request.POST
                doc = DocumentosRegistro()
                org = Organismo()
                ent = Entidad()
                prov = Provincia()
                tdoc = TipoDocumento()
                ent.pk = data['entidad']
                org.pk = data['organismo']
                tdoc.pk = data['tipo_documento']
                prov.pk = data['provincia']
                doc.no_entrada = data['no_entrada_doc']
                doc.no_registro = data['no_registro']
                doc.titulo = request.POST['titulo']
                doc.f_entrada_registro = data['f_entrada_registro']
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


class EditarDocumentoRegistroView(LoginRequiredMixin, UpdateView):
    template_name = "registro_entradas.html"
    form_class = DocumentoRegistroForm
    model = DocumentosRegistro
    login_url = '/entrar/'

    def post(self, request, *args, **kwargs):
        info = {}
        fn = {}
        agregado = {}
        try:
            if request.method == "POST":
                data = request.POST
                if len(data) == 2:
                    no_registro = data['registro']
                    if DocumentosRegistro.objects.get_or_create(no_registro=int(no_registro)):
                        doc = DocumentosRegistro.objects.filter(no_registro=no_registro)
                        for i in doc:
                            fn['pk'] = i.pk
                            fn['no_entrada_doc'] = i.no_entrada
                            fn['no_registro'] = i.no_registro
                            fn['titulo'] = i.titulo
                            fn['f_entrada_registro'] = i.f_entrada_registro
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
                    doc = DocumentosRegistro.objects.filter(no_registro=data['no_registro'])
                    for i in doc:
                        id_doc = i.pk
                    doc_editado = DocumentosRegistro.objects.get(pk=id_doc)
                    doc_editado.no_entrada_doc = data['no_entrada_doc']
                    doc_editado.no_registro = data['no_registro']
                    doc_editado.f_entrada_regisro = data['f_entrada_registro']
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


class EliminarDocumentoRegistroView(LoginRequiredMixin,DeleteView):
    pass


