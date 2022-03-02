from django.forms import ModelForm, TextInput, Textarea, NumberInput, DateField, Select, SelectDateWidget
from control.models import Documento
from tempus_dominus.widgets import DatePicker


# tirala aq

class DocumentoForm(ModelForm):
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
                'placeholder': 'Número consecutivo',
                'style': 'max-width: 300px;'
            }),
            'f_entrada_doc': SelectDateWidget(attrs={
                 'class': "form-control row col4",
                'label': 'Fecha de entrada',
                'placeholder': 'Fecha entrada',
                'style': 'max-width: 100px;'
            }),
        }
