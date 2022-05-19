from django.db import models
from control.models import Documento, Provincia, Entidad, TipoDocumento, Organismo, Direcciones

# Create your models here.


class DocumentosRegistro(models.Model):
    no_registro = models.IntegerField(null=False, blank=False, unique=True)
    no_entrada = models.IntegerField(null=True, blank=True)
    f_entrada_registro = models.DateField(verbose_name="fecha entrada", null=False, blank=False)
    titulo = models.CharField(max_length=255, null=False, blank=False)
    organismo = models.ForeignKey('control.Organismo', on_delete=models.CASCADE)
    entidad = models.ForeignKey('control.Entidad', on_delete=models.CASCADE)
    provincia = models.ForeignKey('control.Provincia', on_delete=models.CASCADE)
    t_documento = models.ForeignKey('control.TipoDocumento', on_delete=models.CASCADE, verbose_name="Tipo de documento")
    observaciones = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Entrada a Registro'
        verbose_name_plural = 'Entradas de Registro'


    def __str__(self):
        return self.titulo



class SalidasRegistro(models.Model):
    no_salida_registro = models.IntegerField(verbose_name="Número de salida registro", null=False, blank=False, unique=True)
    f_salida_registro = models.DateField(verbose_name="fecha de salida registro", null=False, blank=False)
    titulo = models.CharField(max_length=255, null=False, blank=False)
    organismo = models.ForeignKey('control.Organismo', on_delete=models.CASCADE)
    entidad = models.ForeignKey('control.Entidad', on_delete=models.CASCADE)
    provincia = models.ForeignKey('control.Provincia', on_delete=models.CASCADE)
    t_documento_salida = models.ForeignKey('control.TipoDocumentoSalida', on_delete=models.CASCADE,
                                           verbose_name="Tipo de documento de saalida")
    observaciones = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "Salida de registro"
        verbose_name_plural = "Salidas de documentos en registro"

    def __str__(self):
        return self.titulo
