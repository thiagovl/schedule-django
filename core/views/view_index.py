from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from core.models import Evento 

# Create your views here.

def index(request):
    return render(request, "index.html")

# @login_required(login_url="/index/")
# def home(request):
#     usuario = request.user
#     eventos = Evento.objects.filter(usuario=usuario)
#     dados = {'eventos': eventos, 'usuario':usuario}
#     return render(request, 'home.html', dados)

# def login_submit(request):
#     if request.POST:
#         username = request.POST.get('username') # Recuperando os parametros enviados pelo formulário
#         password = request.POST.get('password') # Recuperando os parametros enviados pelo formulário

#         usuario = authenticate(username=username, password=password) # Fazendo a autenticação
#         if usuario is not None:
#             login(request, usuario)
#             return redirect('/')
#         else:
#             messages.error(request, "Usuário ou senha invalido!")
#     return redirect('/')

# def logout_user(request):
#     logout(request)
#     return redirect('/index')

# def visualizar(request, id):
#     evento = Evento.objects.filter(id=id)
#     dados = {'evento': evento}
#     return render(request, 'visualizar.html', dados)

