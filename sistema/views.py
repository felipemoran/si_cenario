# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required

from datetime import *
from sistema.models import *
from sistema.forms import *


def home(request):
    return render(request, 'home.html', locals())


def projeto_lista(request):
    return render(request, 'projeto_lista.html', locals())


def projeto_cadastrar(request):
    novo_projeto = ProjetoForm()

    if request.method == 'POST':
        novo_projeto = ProjetoForm(request.POST)
        if novo_projeto.is_valid():
            novo_projeto.save()

    lista_projetos = Projeto.objects.all()

    return render(request, 'projeto_cadastrar.html', locals())


def projeto_editar(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    novo_projeto = ProjetoForm(instance=projeto)

    if request.method == 'POST':
        novo_projeto = ProjetoForm(request.POST, instance=projeto)
        if novo_projeto.is_valid():
            novo_projeto.save()

    lista_projetos = Projeto.objects.all()

    return render(request, 'projeto_cadastrar.html', locals())


def projeto_deletar(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()

    return HttpResponseRedirect("/home/")


def cadastra_usuario(request):
    form_membro = MembroForm()
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        novo_membro = MembroForm(request.POST)
        print '----------'
        print novo_membro
        if novo_membro.is_valid():
            novo_membro.save()

    return render(request, 'cadastra_usuario.html', locals())
