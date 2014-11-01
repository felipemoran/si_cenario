from models import *
from django import forms


class metaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(metaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'span12'


class ProjetoForm(metaForm):
    class Meta:
        model = Projeto


class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        exclude = ('usuario',)
