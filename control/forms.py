from django.forms import ModelForm, TextInput, Textarea, NumberInput, DateField, Select
from control.models import Documento

#tirala aqui

class DocumentoForm(ModelForm):
    class Meta:
        model = Documento
        fields = ['no_entrada_doc','no_salida_doc','f_entrada_doc','f_salida_doc','titulo','dirigido','organismo',
                  'entidad','t_documento','observaciones']

        widgets = {
            'no_entrada_doc': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Numero entrada'
            }),
            'no_salida_doc': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Numero salida'
            }),
            'f_entrada_doc' : DateField(attrs={
                'class': "datepicker",
                'style': 'max-width: 300px;',
                'placeholder': 'Fecha entrada'
            }),
            'f_salida_doc' : DateField(attrs={
                'class': "datepicker",
                'style': 'max-width: 300px;',
                'placeholder': 'Fecha entrada'
            }),
            'titulo' : TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Título'
            }),
            'dirigido': Select(attrs={
                'class': 'form-select',
                'style': 'max-width: 300px;'
            }),
            'organismo' : Select(attrs={
                'class': 'form-select',
                'style': 'max-width: 300px;'
            }),
            'entidad' : Select(attrs={
                'class': 'form-select',
                'style': 'max-width: 300px;'
            }),
            't_documento': Select(attrs={
                'class': 'form-select',
                'style': 'max-width: 300px;'
            }),
            'observaciones': Textarea(attrs={
                'class': 'form-select',
                'style': 'max-width: 300px;',
                'placeholder': 'Observaciones '
            })
        }





