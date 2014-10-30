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

