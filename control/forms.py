from django import forms
from django.forms import ModelForm, TextInput, Textarea, NumberInput, DateField, Select, SelectDateWidget, DateInput
from control.models import DocumentoSalida, Documento


# tirala aqui

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['no_entrada_doc', 'titulo', 'f_entrada_doc', 'dirigido', 'organismo', 'entidad', 't_documento',
                  'observaciones','f_termino','soporte_doc','forma_entrada','provincia','f_entrega_dirigido']

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
                'style': 'max-width: 100px;',
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
            'f_termino': DateInput(attrs={
                'class': "form-control",
                'type': 'date',
                'label': 'Fecha de término',
                'style': 'max-width: 200px;'
            }),
            'forma_entrada': Select(attrs={
                'class': "form-control",
                'label': 'Forma de entrada del documento',
                'style': 'max-width: 300px;'
            }),
            'soporte_doc': TextInput(attrs={
                'class': "form-control",
                'label': "Soporte",
                'placeholder': 'Soporte en el que se entrega',
                'style': 'max-width: 300px;'
            }),
            'provincia': Select(attrs={
                'class': "form-control",
                'labeel': 'Provincia',
                'style': 'max-width: 300px;'
            }),
            'f_entrega_dirigido': DateInput(attrs={
                'class': "form-control",
                'type': 'date',
                'label': 'Fecha de entrega dirección',
                'style': 'max-width: 200px;'
            }),

        }


class DocumentoSalidaForm(forms.ModelForm):
    class Meta:
        model = DocumentoSalida
        fields = ['no_salida_doc', 'titulo', 'f_salida_doc', 'forma_salida', 'organismo', 'entidad', 't_documento_salida',
                  'observaciones','procedencia','provincia','soporte_doc_salida']

        widgets = {
            'titulo': TextInput(attrs={
                'class': "form-control",
                'label': 'Título',
                'placeholder': 'Titulo documento',
                'style': 'max-width: 500px;'
            }),
            'no_salida_doc': NumberInput(attrs={
                'class': "form-control",
                'label': "Número de entrada",
                'placeholder': 'Número consecutivo',
                'style': 'max-width: 100px;',
                'required': '',
            }),
            'f_salida_doc': DateInput(attrs={
                'class': "form-control",
                'type': 'date',
                'label': 'Fecha de entrada',
                'style': 'max-width: 200px;'
            }),
            'procedencia': Select(attrs={
                'class': "form-control",
                'label': 'Procedencia:',
                'style': 'max-width: 300px;'
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
                'label': 'Dirigido a:',
                'style': 'max-width: 300px;'
            }),
            'observaciones': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Observaciones al documento',
                'style': 'max-width: 500px;'
            }),
            'forma_salida': Select(attrs={
                'class': "form-control",
                'label': 'Forma de entrada del documento',
                'style': 'max-width: 300px;'
            }),
            'provincia': Select(attrs={
                'class': "form-control",
                'labeel': 'Provincia',
                'style': 'max-width: 300px;'
            }),
            'soporte_doc_salida': TextInput(attrs={
                'class': "form-control",
                'label': 'Soporte de documento',
                'placeholder': 'Introduzca el soporte',
                'style': 'max-width: 300px;'
            }),

        }