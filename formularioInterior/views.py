from django.shortcuts import render, redirect
from .forms import UsuarioFormulario
from .models import Usuario
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')

def fazer_login(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        usuario = authenticate(request, cpf=cpf, senha=senha)
        if usuario is not None:
            login(request, usuario)
            # Redirecionar para a página desejada após o login
            return redirect('pagina_desejada')
        else: 
            # Exibir mensagem de erro de login
            return render(request, 'index.html', {'erro_login': True})
    else:
        return render(request, 'pagina_de_login.html')
    


def cadastrar_usuario(request):
    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_usuarios')  # Redireciona para a lista de pessoas (ajuste conforme suas URLs)
    else:
        formulario = UsuarioFormulario()

    return render(request, 'cadastrar_usuario.html', {'form': formulario})

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})