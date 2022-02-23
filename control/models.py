from django.db import models

# Create your models here.


class Direcciones(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()


class Organismo(models.Model):
    nombre = models.CharField(max_length=25)


class Entidad(models.Model):
    nombre = models.CharField(max_length=100)


class TipoDocumento(models.Model):
    tipo = models.CharField(max_length=255)


