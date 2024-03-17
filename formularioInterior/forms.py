
from django import forms
from .models import Usuario

class UsuarioFormulario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nomeUsuario', 'cpfUsuario', 'emailUsuario', 'senhaUsuario', 'codUsuario']
