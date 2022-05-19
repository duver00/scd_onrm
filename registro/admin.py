from django.contrib import admin
from .models import DocumentosRegistro, SalidasRegistro

# Register your models here.


class DocumentoRegistroAdmin(admin.ModelAdmin):
    list_display = ('no_registro','no_entrada','f_entrada_registro','titulo','t_documento','entidad')


class SalidasRegistroAdmin(admin.ModelAdmin):
    list_display = ('no_salida_registro', 'f_salida_registro', 'titulo', 'titulo', 'organismo', 'entidad','provincia','observaciones')


admin.site.register(DocumentosRegistro, DocumentoRegistroAdmin)
admin.site.register(SalidasRegistro, SalidasRegistroAdmin)