from models import *
from django import forms

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto


class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        widgets = {
            'password': forms.PasswordInput(),
        }


