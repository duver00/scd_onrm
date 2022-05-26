from django.contrib import admin
from .models import DocumentosTecnica, SalidasTecnica

# Register your models here.


class DocumentoTecnicaAdmin(admin.ModelAdmin):
    list_display = ('no_tecnica', 'no_entrada', 'f_entrada_tecnica', 'titulo', 't_documento', 'entidad')


class SalidasTecnicaAdmin(admin.ModelAdmin):
    list_display = ('no_salida_tecnica', 'f_salida_tecnica', 'titulo', 'titulo', 'organismo', 'entidad','provincia','observaciones')




admin.site.register(DocumentosTecnica, DocumentoTecnicaAdmin)
admin.site.register(SalidasTecnica, SalidasTecnicaAdmin)