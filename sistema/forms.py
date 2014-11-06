# -*- coding: utf-8 -*-
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


class MembroForm(metaForm):
    class Meta:
        model = Membro
        exclude = ('usuario',)

class LoginForm(forms.Form):
    login = forms.CharField(label=(u'Usuário'), widget=forms.TextInput(attrs={'class':'text'}))
    senha = forms.CharField(label=(u'Senha'), widget=forms.PasswordInput(attrs={'class':'text'}))
