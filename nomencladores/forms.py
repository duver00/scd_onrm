from django import forms
from django.forms import TextInput
from control.models import Entidad, TipoDocumentoSalida, TipoDocumento, Direcciones, Organismo, Provincia


class EntidadForm(forms.ModelForm):
    class Meta:
        model = Entidad
        fields = ['nombre']

        widgets = {
            'nombre': TextInput(attrs={
                'class': "form-control",
                'label': 'Nombre de la entidad',
                'placeholder': 'Introduzca el nombre de la entidad',
                'style': 'max-width: 500px;'
            }),
        }



class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = ['nombre']

        widgets = {
            'nombre': TextInput(attrs={
                'class': "form-control",
                'label': 'Nombre de la provincia',
                'placeholder': 'Introduzca el nombre de la provincia',
                'style': 'max-width: 500px;'
            }),
        }


class DireccionesForm(forms.ModelForm):
    class Meta:
        model = Direcciones
        fields = ['nombre','correo']

        widgets = {
            'nombre': TextInput(attrs={
                'class': "form-control",
                'label': 'Nombre de la provincia',
                'placeholder': 'Introduzca el nombre de la provincia',
                'style': 'max-width: 500px;'
            }),
            'correo': TextInput(attrs={
                'class': "form-control",
                'type':'email',
                'label': 'Nombre de la provincia',
                'placeholder': 'Introduzca el nombre de la provincia',
                'style': 'max-width: 500px;'
            }),
        }


class OrganismoForm(forms.ModelForm):
    class Meta:
        model = Organismo
        fields = ['nombre']

        widgets = {
            'nombre': TextInput(attrs={
                'class': "form-control",
                'label': 'Nombre del organismo',
                'placeholder': 'Introduzca el organismo',
                'style': 'max-width: 500px;'
            }),
        }


class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = ['tipo']

        widgets = {
            'nombre': TextInput(attrs={
                'class': "form-control",
                'label': 'Tipo de documento',
                'placeholder': 'Introduzca el tipo',
                'style': 'max-width: 500px;'
            }),
        }





class TipoDocumentoSalidaForm(forms.ModelForm):
    class Meta:
        model = TipoDocumentoSalida
        fields = ['tipo']

        widgets = {
            'nombre': TextInput(attrs={
                'class': "form-control",
                'label': 'Tipo de documento de salida',
                'placeholder': 'Introduzca el tipo',
                'style': 'max-width: 500px;'
            }),
        }
