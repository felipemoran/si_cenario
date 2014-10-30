from models import *
from django import forms

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto


