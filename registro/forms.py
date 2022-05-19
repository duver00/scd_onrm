from django import forms
from .models import DocumentosRegistro, SalidasRegistro
from django.forms.widgets import TextInput, NumberInput, DateInput, Select, Textarea


class DocumentoRegistroForm(forms.ModelForm):
    class Meta:
        model = DocumentosRegistro
        fields = ['no_registro', 'no_entrada', 'titulo', 'f_entrada_registro', 'organismo', 'entidad', 't_documento',
                  'observaciones', 'provincia']

        widgets = {
            'titulo': TextInput(attrs={
                'class': "form-control",
                'label': 'Título',
                'placeholder': 'Titulo documento',
                'style': 'max-width: 500px;'
            }),
            'no_entrada': NumberInput(attrs={
                'class': "form-control",
                'label': "Número de entrada documentación",
                'placeholder': 'Número consecutivo',
                'style': 'max-width: 100px;',
                'required': '',
            }),
            'no_registro': NumberInput(attrs={
                'class': "form-control",
                'label': "Número de entrada registro",
                'placeholder': 'Número consecutivo',
                'style': 'max-width: 100px;',
                'required': '',
            }),
            'f_entrada_registro': DateInput(attrs={
                'class': "form-control",
                'type': 'date',
                'label': 'Fecha de entrada registro',
                'style': 'max-width: 200px;'
            }),
            'organismo': Select(attrs={
                'class': "form-control",
                'label': 'Organismo:',
                'placeholder': 'Organismo al que pertenece',
                'style': 'max-width: 300px;'
            }),
            'entidad': Select(attrs={
                'class': "form-control",
                'label': 'Entidad:',
                'style': 'max-width: 300px;'
            }),
            't_documento': Select(attrs={
                'class': "form-control",
                'label': 'Dirigido a:',
                'style': 'max-width: 300px;'
            }),
            'observaciones': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Observaciones al documento',
                'style': 'max-width: 500px;'
            }),
            'provincia': Select(attrs={
                'class': "form-control",
                'labeel': 'Provincia',
                'style': 'max-width: 300px;'
            }),

        }


class SalidaRegistroForm(forms.ModelForm):
    class Meta:
        model = SalidasRegistro
        fields = ['no_salida_registro', 'f_salida_registro', 'titulo', 'organismo', 'entidad','provincia','t_documento_salida','observaciones']

        widgets = {
            'titulo': TextInput(attrs={
                'class': "form-control",
                'label': 'Título',
                'placeholder': 'Titulo documento',
                'style': 'max-width: 500px;'
            }),
            'no_salida_registro': NumberInput(attrs={
                'class': "form-control",
                'label': "Número de salida",
                'placeholder': 'Número consecutivo',
                'style': 'max-width: 100px;',
                'required': '',
            }),
            'f_salida_registro': DateInput(attrs={
                'class': "form-control",
                'type': 'date',
                'label': 'Fecha de salida',
                'style': 'max-width: 200px;'
            }),
            'organismo': Select(attrs={
                'class': "form-control",
                'label': 'Organismo:',
                'placeholder': 'Organismo al que pertenece',
                'style': 'max-width: 300px;'
            }),
            'entidad': Select(attrs={
                'class': "form-control",
                'label': 'Entidad:',
                'style': 'max-width: 300px;'
            }),
            't_documento_salida': Select(attrs={
                'class': "form-control",
                'label': 'Tipo de documento de salida',
                'style': 'max-width: 300px;'
            }),
            'observaciones': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Observaciones al documento',
                'style': 'max-width: 500px;'
            }),
            'provincia': Select(attrs={
                'class': "form-control",
                'labeel': 'Provincia',
                'style': 'max-width: 300px;'
            }),

        }
