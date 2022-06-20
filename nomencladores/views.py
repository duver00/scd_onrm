from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from control.models import Entidad, Provincia, Organismo, TipoDocumentoSalida, TipoDocumento, Direcciones
from .forms import EntidadForm, ProvinciaForm, OrganismoForm, DireccionesForm, TipoDocumentoForm,  TipoDocumentoSalidaForm
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


class NuevoNomencladorView(PermissionRequiredMixin, CreateView):
    template_name = "nomencladores.html"
    permission_required = 'nomencladores.add_all'
    login_url = '/entrar/'

    def post(self, request, *args, **kwargs):
        info = {}
        try:
            if request.method == 'POST':
                data = request.POST               
                if len(data)== 4 and data['action'] == 'direcciones':                    
                    dir = Direcciones()
                    dir.nombre = data['nombre']
                    dir.correo = data['correo']
                    dir.save()                    
                    return JsonResponse(data)
                elif data['action'] == 'provincia':
                    prov = Provincia()
                    prov.nombre = data['nombre']
                    prov.save()
                    return JsonResponse(data)
                if data['action'] == 'organismo':
                    org = Organismo()
                    org.nombre = data['nombre']
                    org.save()
                    return JsonResponse(data)
                if data['action'] == 'entidad':
                    ent = Entidad()
                    ent.nombre = data['nombre']
                    ent.save()
                    return JsonResponse(data)
                elif data['action'] == 'tdoc':
                    tdoc = TipoDocumento()
                    tdoc.tipo = data['nombre']
                    tdoc.save()
                    return JsonResponse(data)
                if data['action'] == 'tdoc_salida':
                    tdoc_salida = TipoDocumentoSalida()
                    tdoc_salida.tipo = data['nombre']
                    tdoc_salida.save()
                    return JsonResponse(data)              
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)


class EditarNomencladorView(PermissionRequiredMixin, UpdateView):
    template_name = "nomencladores.html"
    permission_required = 'nomencladores.update_all'
    login_url = '/entrar/'


    def post(self, request, *args, **kwargs):
        info = {}
        fn = {}
        try:
            if request.method == 'POST':
                data = request.POST       
                if len(data) == 3 and data['nombre'] == 'direccion':
                    print('dentro')
                    if Direcciones.objects.get_or_create(pk=data['pk']):
                        direccion = Direcciones.objects.get(pk=data['pk'])
                        fn['pk'] = direccion.pk
                        fn['nombre'] = direccion.nombre
                        fn['correo'] = direccion.correo
                        return JsonResponse(fn)
                elif len(data) == 5 and data['action'] == 'edited_direccion':                
                    print('mas adentro')
                    direccion = Direcciones.objects.get(pk=data['pk'])
                    direccion.nombre = data['nombre']
                    direccion.correo = data['correo']
                    direccion.save()
                    info['ok'] = 'editado'
                    print('asdas')
                    return JsonResponse(data)
                if len(data) == 3 and data['nombre'] == 'entidad':
                    print('dentro entidad')
                    if Entidad.objects.get_or_create(pk=data['pk']):
                        entidad = Entidad.objects.get(pk=data['pk'])
                        fn['pk'] = entidad.pk
                        fn['nombre'] = entidad.nombre
                        return JsonResponse(fn)
                elif len(data) == 4 and data['post_action'] == 'entidad':
                        entidad = Entidad.objects.get(pk=data['pk'])
                        entidad.nombre = data['nombre']                        
                        entidad.save()
                        info['ok'] = 'Entidad Editada'              
                        return JsonResponse(data)  
                if len(data) == 3 and data['nombre'] == 'organismo':
                    print('dentro organismo')
                    if Organismo.objects.get_or_create(pk=data['pk']):
                        organismo = Organismo.objects.get(pk=data['pk'])
                        fn['pk'] = organismo.pk
                        fn['nombre'] = organismo.nombre
                        return JsonResponse(fn)
                elif len(data) == 4 and data['post_action'] == 'organismo':
                        organismo = Organismo.objects.get(pk=data['pk'])
                        organismo.nombre = data['nombre']                        
                        organismo.save()
                        info['ok'] = 'Organismo Editado'              
                        return JsonResponse(data)
                if len(data) == 3 and data['nombre'] == 'provincia':
                    print('dentro provincia')
                    if Provincia.objects.get_or_create(pk=data['pk']):
                        provincia = Provincia.objects.get(pk=data['pk'])
                        fn['pk'] = provincia.pk
                        fn['nombre'] = provincia.nombre
                        return JsonResponse(fn)
                elif len(data) == 4 and data['post_action'] == 'provincia':
                        provincia = Provincia.objects.get(pk=data['pk'])
                        provincia.nombre = data['nombre']                        
                        provincia.save()
                        info['ok'] = 'Provincia Editada'              
                        return JsonResponse(data)
                if len(data) == 3 and data['nombre'] == 'tdoc_salida':
                    print('dentro salida')
                    if TipoDocumentoSalida.objects.get_or_create(pk=data['pk']):
                        tdoc_salida = TipoDocumentoSalida.objects.get(pk=data['pk'])
                        fn['pk'] = tdoc_salida.pk
                        fn['nombre'] = tdoc_salida.tipo
                        return JsonResponse(fn)
                elif len(data) == 4 and data['post_action'] == 'tdoc_salida':
                        tdoc_salida = TipoDocumentoSalida.objects.get(pk=data['pk'])
                        tdoc_salida.tipo = data['nombre']                        
                        tdoc_salida.save()
                        info['ok'] = 'Tipo de salida Editada'              
                        return JsonResponse(data)
                if len(data) == 3 and data['nombre'] == 'tdoc':
                    print('dentro entrada')
                    if TipoDocumento.objects.get_or_create(pk=data['pk']):
                        tdoc = TipoDocumento.objects.get(pk=data['pk'])
                        fn['pk'] = tdoc.pk
                        fn['nombre'] = tdoc.tipo
                        return JsonResponse(fn)
                elif len(data) == 4 and data['post_action'] == 'tdoc':
                        tdoc = TipoDocumento.objects.get(pk=data['pk'])
                        tdoc.tipo = data['nombre']                        
                        tdoc.save()
                        info['ok'] = 'Tipo de entrada Editada'              
                        return JsonResponse(data)                            
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)


class EliminarNomencladorView(PermissionRequiredMixin, DeleteView):
    template_name = "nomencladores.html"
    permission_required = 'nomencladores.delete_all'
    login_url = '/entrar/'
    model = Direcciones

    def post(self, request, *args, **kwargs):
        info = {}
        dat = {}
        try:
            if request.method == "POST":
                data = request.POST
                if data['direccion'] == 'direccion':
                    direccion = Direcciones.objects.get(pk=data['valor'])                   
                    direccion.delete()
                    dat['datos'] = 'Direccion Eliminada'
                    return JsonResponse(dat)     
                elif data['direccion'] == 'entidad':
                    entidad = Entidad.objects.get(pk=data['valor'])                    
                    entidad.delete()
                    dat['datos'] = 'Entidad Eliminada'
                    return JsonResponse(dat) 
                elif data['direccion'] == 'organismo':
                    organismo = Organismo.objects.get(pk=data['valor'])                    
                    organismo.delete()
                    dat['datos'] = 'Organismo Eliminado'
                    return JsonResponse(dat)
                elif data['direccion'] == 'provincia':
                    provincia = Provincia.objects.get(pk=data['valor'])                    
                    provincia.delete()
                    dat['datos'] = 'Provincia Eliminada'
                    return JsonResponse(dat)
                elif data['direccion'] == 'tdoc_salida':
                    tdoc_salida = TipoDocumentoSalida.objects.get(pk=data['valor'])                    
                    tdoc_salida.delete()
                    dat['datos'] = 'Tipo documento salida Eliminada'
                    return JsonResponse(dat)
                elif data['direccion'] == 'tdoc':
                    tdoc = TipoDocumento.objects.get(pk=data['valor'])                    
                    tdoc.delete()
                    dat['datos'] = 'tipo documento entrada Eliminada'
                    return JsonResponse(dat)
                    
        except Exception as e:
            info['error'] = str(e)
            return JsonResponse(info)





