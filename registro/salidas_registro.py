from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SalidasRegistro
from .forms import SalidaRegistroForm
from control.models import Direcciones, Entidad, Organismo, Provincia, TipoDocumentoSalida
from django.http import JsonResponse


class SalidaRegistroView(LoginRequiredMixin, TemplateView):
    template_name = "registro_salidas.html"
    login_url = '/entrar/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_salidas'] = SalidaRegistroForm()
        context['no_salida_registro'] = SalidasRegistro.objects.all().last()
        context['list_tipos_documentos'] = TipoDocumentoSalida.objects.all()
        context['list_organismos'] = Organismo.objects.all()
        context['list_direcciones'] = Direcciones.objects.all()
        context['list_provincias'] = Provincia.objects.all()
        context['list_entidad'] = Entidad.objects.all()
        context['list_salidas'] = SalidasRegistro.objects.all()
        return context


class NuevaSalidaRegistroView(LoginRequiredMixin, CreateView):
    template_name = "registro_salidas.html"
    form_class = SalidaRegistroForm
    model = SalidasRegistro
    login_url = '/entrar/'


    def post(self, request, *args, **kwargs):
        info = {}
        try:
            if request.method == 'POST':
                data = request.POST
                doc = SalidasRegistro()
                org = Organismo()
                ent = Entidad()
                prov = Provincia()
                tdoc = TipoDocumentoSalida()
                ent.pk = data['entidad']
                org.pk = data['organismo']
                tdoc.pk = data['tipo_documento']
                prov.pk = data['provincia']
                doc.no_salida_registro = data['no_salida_registro']
                doc.titulo = data['titulo']
                doc.f_salida_registro = data['f_salida_registro']
                doc.organismo = org
                doc.entidad = ent
                doc.t_documento_salida = tdoc
                doc.provincia = prov
                doc.observaciones = data['observaciones']
                doc.save()
                return JsonResponse(data)
            else:
                info['error'] = 'Existe un error '
        except Exception as e:
            print('no entra')
            info['error'] = str(e)
            return JsonResponse(info)


class EditarSalidaRegistroView(LoginRequiredMixin, UpdateView):
    template_name = "registro_salidas.html"
    form_class = SalidaRegistroForm
    model = SalidasRegistro
    login_url = '/entrar/'

    def post(self, request, *args, **kwargs):
        info = {}
        fn = {}
        agregado = {}
        try:
            if request.method == "POST":
                data = request.POST
                if len(data) == 2:
                    if SalidasRegistro.objects.get_or_create(no_salida_registro=data['registro']):
                        doc = SalidasRegistro.objects.filter(no_salida_registro=data['registro'])
                        for i in doc:
                            fn['pk'] = i.pk
                            fn['no_salida_registro'] = i.no_salida_registro
                            fn['titulo'] = i.titulo
                            fn['f_salida_registro'] = i.f_salida_registro
                            fn['entidad'] = i.entidad.pk
                            fn['organismo'] = i.organismo.pk
                            fn['tipo_documento'] = i.t_documento_salida.pk
                            fn['observaciones'] = i.observaciones
                            fn['provincia'] = i.provincia.pk
                    return JsonResponse(fn)
                elif len(data) > 2:
                    org = Organismo()
                    ent = Entidad()
                    tdoc = TipoDocumentoSalida()
                    prov = Provincia()
                    ent.pk = data['entidad']
                    org.pk = data['organismo']
                    tdoc.pk = data['tipo_documento']
                    prov.pk = data['provincia']
                    doc = SalidasRegistro.objects.filter(no_salida_registro=data['no_salida_registro'])
                    for i in doc:
                        id_doc = i.pk
                        break
                    doc_editado = SalidasRegistro.objects.get(pk=id_doc)
                    doc_editado.no_registro = data['no_salida_registro']
                    doc_editado.f_salida_registro = data['f_salida_registro']
                    doc_editado.titulo = data['titulo']
                    doc_editado.organismo = org
                    doc_editado.entidad = ent
                    doc_editado.t_documento_salida = tdoc
                    doc_editado.provincia = prov
                    doc_editado.observaciones = data['observaciones']
                    doc_editado.save()
                    agregado['ok'] = 'editado'
                    return JsonResponse(agregado)
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)


class EliminarSalidaRegistroView(LoginRequiredMixin,DeleteView):
    model = SalidasRegistro
    login_url = '/entrar/'

    def post(self, request, *args, **kwargs):
        info = {}
        dat = {}
        try:
            if request.method == "POST":
                data = request.POST
                documento = SalidasRegistro.objects.filter(no_registro=data['registro'])
                for i in documento:
                    id_doc = i.pk
                    break
                doc = SalidasRegistro.objects.get(pk=id_doc)
                dat['datos'] = doc
                doc.delete()
                return JsonResponse(dat)
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)