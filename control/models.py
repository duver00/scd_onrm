from django.db import models


# Create your models here.


class Direcciones(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    correo = models.EmailField(null=False, blank=False)

    class Meta:
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'

    def __str__(self):
        return self.nombre


class Organismo(models.Model):
    nombre = models.CharField(max_length=25, null=False, blank=False)

    class Meta:
        verbose_name = 'Organismo'
        verbose_name_plural = 'Organismos'

    def __str__(self):
        return self.nombre


class Entidad(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'

    def __str__(self):
        return self.nombre


class TipoDocumento(models.Model):
    tipo = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documentos'

    def __str__(self):
        return self.tipo


class Provincia(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return self.nombre


class Documento(models.Model):
    Entrada = [
        ('Correo', 'Correo'),
        ('Correo electrónico', 'Correo electrónico'),
        ('Mensajeria', 'Mensajeria'),
        ('Fax', 'Fax'),
        ('Personal', 'Personal'),
    ]
    no_entrada_doc = models.IntegerField(verbose_name="Número de entrada", null=False, blank=False, unique=True)
    f_entrada_doc = models.DateField(verbose_name="fecha entrada", null=False, blank=False)
    forma_entrada = models.CharField(choices=Entrada, default='', max_length=55)
    titulo = models.CharField(max_length=255, null=False, blank=False)
    dirigido = models.ForeignKey("Direcciones", on_delete=models.CASCADE, verbose_name="Dirigido a:")
    f_entrega_dirigido = models.DateField(verbose_name="Fecha de entrega", null=False, blank=False)
    organismo = models.ForeignKey('Organismo', on_delete=models.CASCADE)
    entidad = models.ForeignKey('Entidad', on_delete=models.CASCADE)
    provincia = models.ForeignKey('Provincia', on_delete=models.CASCADE)
    t_documento = models.ForeignKey('TipoDocumento', on_delete=models.CASCADE, verbose_name="Tipo de documento")
    soporte_doc = models.CharField(max_length=55, null=False, blank=False)
    f_termino = models.DateField(verbose_name="Fecha de término", null=True, blank=True)
    observaciones = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ['no_entrada_doc']

    def __str__(self):
        return self.titulo


class TipoDocumentoSalida(models.Model):
    tipo = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documentos'

    def __str__(self):
        return self.tipo


class SalidaDocumento(models.Model):
    Salida = [
        ('Correo', 'Correo'),
        ('Correo electrónico', 'Correo electrónico'),
        ('Mensajeria', 'Mensajeria'),
        ('Fax', 'Fax'),
        ('Personal', 'Personal'),
    ]
    no_salida_doc = models.IntegerField(verbose_name="Número de salida", null=False, blank=False, unique=True)
    f_salida_doc = models.DateField(verbose_name="fecha de salida", null=False, blank=False)
    forma_salida = models.CharField(choices=Salida, default='', max_length=55)
    titulo = models.CharField(max_length=255, null=False, blank=False)
    procedencia = models.ForeignKey("Direcciones", on_delete=models.CASCADE, verbose_name="Procedencia:")
    organismo = models.ForeignKey('Organismo', on_delete=models.CASCADE)
    entidad = models.ForeignKey('Entidad', on_delete=models.CASCADE)
    provincia = models.ForeignKey('Provincia', on_delete=models.CASCADE)
    t_documento_salida = models.ForeignKey('TipoDocumentoSalida', on_delete=models.CASCADE,
                                    verbose_name="Tipo de documento de saalida")
    soporte_doc_salida = models.CharField(max_length=55, null=False, blank=False)

    class Meta:
        verbose_name = "Salida de Documento"
        verbose_name_plural = "Salidas de Documentos"

    def __str__(self):
        return self.titulo

