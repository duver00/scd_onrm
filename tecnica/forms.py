from django import forms
from .models import DocumentosTecnica, SalidasTecnica
from django.forms.widgets import TextInput, NumberInput, DateInput, Select, Textarea



class DocumentoTecnicaForm(forms.ModelForm):
    class Meta:
        model = DocumentosTecnica
        fields = ['no_tecnica', 'no_entrada', 'titulo', 'f_entrada_tecnica', 'organismo', 'entidad', 't_documento',
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
            'no_tecnica': NumberInput(attrs={
                'class': "form-control",
                'label': "Número de entrada técnica",
                'placeholder': 'Número consecutivo',
                'style': 'max-width: 100px;',
                'required': '',
            }),
            'f_entrada_tecnica': DateInput(attrs={
                'class': "form-control",
                'type': 'date',
                'label': 'Fecha de entrada técnica',
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


class SalidaTecnicaForm(forms.ModelForm):
    class Meta:
        model = SalidasTecnica
        fields = ['no_salida_tecnica', 'f_salida_tecnica', 'titulo', 'organismo', 'entidad','provincia','t_documento_salida','observaciones']

        widgets = {
            'titulo': TextInput(attrs={
                'class': "form-control",
                'label': 'Título',
                'placeholder': 'Titulo documento',
                'style': 'max-width: 500px;'
            }),
            'no_salida_tecnica': NumberInput(attrs={
                'class': "form-control",
                'label': "Número de salida",
                'placeholder': 'Número consecutivo',
                'style': 'max-width: 100px;',
                'required': '',
            }),
            'f_salida_tecnica': DateInput(attrs={
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
