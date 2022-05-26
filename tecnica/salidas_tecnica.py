from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from .models import SalidasTecnica
from .forms import SalidaTecnicaForm
from control.models import TipoDocumentoSalida, Organismo, Entidad, Provincia, Direcciones


class SalidaTecnicaView(LoginRequiredMixin,PermissionRequiredMixin, TemplateView):
    template_name = "tecnica_salidas.html"
    permission_required = 'tecnica.view_salidastecnica'
    login_url = '/entrar/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_salidas'] = SalidaTecnicaForm()
        context['no_salida_tecnica'] = SalidasTecnica.objects.all().last()
        context['list_tipos_documentos'] = TipoDocumentoSalida.objects.all()
        context['list_organismos'] = Organismo.objects.all()
        context['list_direcciones'] = Direcciones.objects.all()
        context['list_provincias'] = Provincia.objects.all()
        context['list_entidad'] = Entidad.objects.all()
        context['list_salidas'] = SalidasTecnica.objects.all()
        return context


class NuevoSalidaTecnicaView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    template_name = "tecnica_salidas.html"
    model = SalidasTecnica
    form_class = SalidaTecnicaForm
    permission_required = 'tecnica.add_salidastecnica'
    login_url = '/entrar/'


    def post(self, request, *args, **kwargs):
        info = {}
        try:
            if request.method == 'POST':
                data = request.POST
                doc = SalidasTecnica()
                org = Organismo()
                ent = Entidad()
                prov = Provincia()
                tdoc = TipoDocumentoSalida()
                ent.pk = data['entidad']
                org.pk = data['organismo']
                tdoc.pk = data['tipo_documento']
                prov.pk = data['provincia']
                doc.no_salida_tecnica = data['no_salida_tecnica']
                doc.titulo = data['titulo']
                doc.f_salida_tecnica = data['f_salida_tecnica']
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
            info['error'] = str(e)
            return JsonResponse(info)


class EditarSalidaTecnicaView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    template_name = "tecnica_salidas.html"
    form_class = SalidaTecnicaForm
    model = SalidasTecnica
    permission_required = 'tecnica.change_salidastecnica'
    login_url = '/entrar/'

    def post(self, request, *args, **kwargs):
        info = {}
        fn = {}
        agregado = {}
        try:
            if request.method == "POST":
                data = request.POST
                if len(data) == 2:
                    if SalidasTecnica.objects.get_or_create(no_salida_tecnica=data['tecnica']):
                        doc = SalidasTecnica.objects.filter(no_salida_tecnica=data['tecnica'])
                        print(doc)
                        for i in doc:
                            fn['pk'] = i.pk
                            fn['no_salida_tecnica'] = i.no_salida_tecnica
                            fn['titulo'] = i.titulo
                            fn['f_salida_tecnica'] = i.f_salida_tecnica
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
                    doc = SalidasTecnica.objects.filter(no_salida_tecnica=data['no_salida_tecnica'])
                    for i in doc:
                        id_doc = i.pk
                        break
                    doc_editado = SalidasTecnica.objects.get(pk=id_doc)
                    doc_editado.no_salida_tecnica = data['no_salida_tecnica']
                    doc_editado.f_salida_tecnica = data['f_salida_tecnica']
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


class EliminarSalidaTecnicaView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = SalidasTecnica
    permission_required = 'tecnica.delete_salidastecnica'
    login_url = '/entrar/'

    def post(self, request, *args, **kwargs):
        info = {}
        dat = {}
        try:
            if request.method == "POST":
                data = request.POST
                documento = SalidasTecnica.objects.filter(no_salida_tecnica=data['tecnica'])
                for i in documento:
                    id_doc = i.pk
                    break
                doc = SalidasTecnica.objects.get(pk=id_doc)
                dat['datos'] = "Documento Eliminado"
                doc.delete()
                return JsonResponse(dat)
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)


