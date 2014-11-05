from models import *
from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.forms.models import ModelMultipleChoiceField


class metaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(metaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'span12'


class CustomSelectMultiple(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "%s %s " %(obj.nome, obj.sobrenome)


class ProjetoForm(metaForm):
    class Meta:
        model = Projeto
        # exclude = ('membros',)
    # membros = CustomSelectMultiple(widget=forms.CheckboxSelectMultiple, queryset=Membro.objects.all())


class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        exclude = ('usuario',)


class NucleoForm(forms.ModelForm):
    class Meta:
        model = Nucleo

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        exclude = ('membro',)

