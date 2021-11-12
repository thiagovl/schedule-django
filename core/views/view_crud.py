from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Evento 
from django.http.response import Http404
from django.contrib.auth.models import User

# Visualizar evento
@login_required(login_url='/login/')
def visualizar(request, id):
    evento = Evento.objects.filter(id=id)
    dados = {'evento': evento}
    return render(request, 'visualizar.html', dados)


@login_required(login_url='/login/')
def salvar_ediar(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_evento = request.POST.get('data_evento')
        hora = request.POST.get('hora')
        usuario = request.user
        data_evento = str(data_evento)+'T'+str(hora) # Concatenando a data_evento e hora
        status = request.POST.get('status')
        id_evento = request.POST.get('id_evento')

        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.status = status
                evento.save()

        else:
            Evento.objects.create(
                titulo=titulo,
                descricao=descricao,
                data_evento=data_evento,
                usuario=usuario,
                status=status
            )
    return redirect('/')

@login_required(login_url='/login/')
def editar(request):
    id_evento = request.GET.get('id_evento')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def deletar(request, id):
    try:
        evento = Evento.objects.get(id=id)
    except Exception:
        raise Http404()

    usuario = request.user
    evento = Evento.objects.get(id=id)

    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')

def cadastrar(request):
    return render(request, 'signup.html')

def registrar(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    password = request.POST.get('password')
    user=User.objects.create_user(nome, email=email, password=password)
    user.is_superuser=False
    user.is_staff=False
    user.save()
    return redirect('/')