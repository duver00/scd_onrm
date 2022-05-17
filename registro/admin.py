from django.contrib import admin
from .models import DocumentosRegistro

# Register your models here.


class DocumentoRegistroAdmin(admin.ModelAdmin):
    list_display = ('no_registro','no_entrada','f_entrada_registro','titulo','t_documento','entidad')



admin.site.register(DocumentosRegistro, DocumentoRegistroAdmin)