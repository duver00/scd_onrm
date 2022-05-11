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


class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)


class DocumentoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "f_entrada_doc", "f_entrega_dirigido", "dirigido", "no_entrada_doc", )
    list_filter = ( "organismo", "entidad", "dirigido")

class SalidaDocumentoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "f_salida_doc", "entidad", "procedencia", "no_salida_doc",)
    list_filter = ("organismo", "provincia", "t_documento_salida")



admin.site.register(Direcciones, DireccionesAdmin)
admin.site.register(Organismo, OrganismoAdmin )
admin.site.register(Entidad, EntidadAdmin)
admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(SalidaDocumento, SalidaDocumentoAdmin)
