from django.contrib import admin
from .models import *


# Register your models here.
class DireccionesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "correo")


class OrganismoAdmin(admin.ModelAdmin):
    list_display = ("nombre",)


class EntidadAdmin(admin.ModelAdmin):
    list_display = ("nombre",)


class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ("tipo",)


class DocumentoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "f_entrada_doc", "f_salida_doc", "dirigido", "no_entrada_doc", "no_salida_doc")
    list_filter = ( "organismo", "entidad", "dirigido")


admin.site.register(Direcciones, DireccionesAdmin)
admin.site.register(Organismo, OrganismoAdmin )
admin.site.register(Entidad, EntidadAdmin)
admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(Documento, DocumentoAdmin)
