from django.db import models


# Create your models here.


class Direcciones(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    correo = models.EmailField(null=False, blank=False)


class Organismo(models.Model):
    nombre = models.CharField(max_length=25, null=False, blank=False)

    class Meta:
        verbose_name = 'Organismo'
        verbose_name_plural = 'Organismo'


class Entidad(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'


class TipoDocumento(models.Model):
    tipo = models.CharField(max_length=255,null=False, blank=False)

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documentos'


class Documento(models.Model):
    no_entrada_doc = models.IntegerField(null=False,blank=False)
    no_salida_doc = models.IntegerField(null=True, blank=True)
    f_entrada_doc = models.DateField(null=False, blank=False)
    f_salida_doc = models.DateField(null=True, blank=True)
    titulo = models.CharField(max_length=255)
    organismo = models.ForeignKey('Organismo', on_delete=models.CASCADE)
    entidad = models.ForeignKey('Entidad', on_delete=models.CASCADE)
    t_documento = models.ForeignKey('TipoDocumento', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'


