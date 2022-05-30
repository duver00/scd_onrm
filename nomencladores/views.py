from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from control.models import Entidad, Provincia, Organismo, TipoDocumentoSalida, TipoDocumento, Direcciones
from .forms import EntidadForm, ProvinciaForm, OrganismoForm, DireccionesForm, TipoDocumentoForm, TipoDocumentoSalidaForm
from django.http import JsonResponse


# Create your views here.


class NomencladoresView(PermissionRequiredMixin, TemplateView):
    template_name = "nomencladores.html"
    permission_required = 'nomencladores.view_entidad'
    login_url = '/entrar/'

    def get_context_data(self, **kwargs):
        context = super(NomencladoresView, self).get_context_data(**kwargs)
        context['list_entidad'] = Entidad.objects.all()
        context['form_entidad'] = EntidadForm()
        context['list_direcciones'] = Direcciones.objects.all()
        context['form_direcciones'] = DireccionesForm()
        context['list_provincia'] = Provincia.objects.all()
        context['form_provincia'] = ProvinciaForm()
        context['list_organismo'] = Organismo.objects.all()
        context['form_organismo'] = OrganismoForm()
        context['list_t_documento'] = TipoDocumento.objects.all()
        context['form_t_documento'] = TipoDocumentoForm()
        context['list_t_documento_salida'] = TipoDocumentoSalida.objects.all()
        context['form_t_documento_salida'] = TipoDocumentoSalidaForm()
        return context


class NuevoNomencadorView(PermissionRequiredMixin, CreateView):
    template_name = "nomencladores.html"
    permission_required = 'nomencladores.add_entidad'
    login_url = '/entrar/'

    def post(self, request, *args, **kwargs):
        info = {}
        try:
            if request.method == 'POST':
                data = request.POST
                if data['action'] =='entidad':
                    ent = Entidad()
                    ent.pk = data['nombre']
                    ent.save()
                    return JsonResponse(data)
            else:
                info['error'] = 'Existe un error '
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)



class EditarNomencladoresVire(PermissionRequiredMixin, UpdateView):
    template_name = "nomencladores.html"
    permission_required = 'nomencladores.update_entidad'
    login_url = '/entrar/'

    def post(self, request, *args, **kwargs):
        pass
