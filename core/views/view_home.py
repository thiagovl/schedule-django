from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Evento 

@login_required(login_url="/index/")
def home(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': eventos, 'usuario':usuario}
    return render(request, 'home.html', dados)

@login_required(login_url='/login/')
def adicionar(request):
    return render(request, 'evento.html')