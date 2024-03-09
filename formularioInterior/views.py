from django.shortcuts import render, redirect
from .forms import PessoaFormulario
from .models import Pessoa

def index(request):
    return render(request, 'index.html')


def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')  # Redireciona para a lista de pessoas (ajuste conforme suas URLs)
    else:
        form = PessoaFormulario()

    return render(request, 'cadastrar_pessoa.html', {'form': form})

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'listar_pessoas.html', {'pessoas': pessoas})