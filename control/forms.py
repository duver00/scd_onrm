from django import forms
from django.forms import ModelForm, TextInput, Textarea, NumberInput, DateField, Select, SelectDateWidget, DateInput
from control.models import Documento


# tirala aq

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['no_entrada_doc', 'titulo', 'f_entrada_doc', 'dirigido', 'organismo', 'entidad', 't_documento',
                  'observaciones']

        widgets = {
            'titulo': TextInput(attrs={
                'class': "form-control",
                'label': 'Título',
                'placeholder': 'Titulo documento',
                'style': 'max-width: 500px;'
            }),
            'no_entrada_doc': NumberInput(attrs={
                'class': "form-control",
                'label': "Número de entrada",
                'placeholder': 'Número consecutivo',
                'style': 'max-width: 200px;',
                'required': '',
            }),
            'f_entrada_doc': DateInput(attrs={
                'class': "form-control",
                'type': 'date',
                'label': 'Fecha de entrada',
                'style': 'max-width: 200px;'
            }),
            'dirigido': Select(attrs={
                'class': "form-control",
                'label': 'Dirigido a:',
                'style': 'max-width: 300px;'
            }),
            'organismo': Select(attrs={
                'class': "form-control",
                'label': 'Organismo:',
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

        }
