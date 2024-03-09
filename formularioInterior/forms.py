
from django import forms
from .models import Pessoa

class PessoaFormulario(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'cpf']
