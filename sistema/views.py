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


def teste(request):
    return render(request, 'teste.html', locals())


def projeto_lista(request):
    lista_projetos = Projeto.objects.all()

    return render(request, 'projeto_lista.html', locals())


def projeto_cadastrar(request):
    novo_projeto = ProjetoForm()
    if request.method == 'POST':
        novo_projeto = ProjetoForm(request.POST)
        print novo_projeto
        if novo_projeto.is_valid():
            projeto = novo_projeto.save(commit=False)
            projeto.save()
            return HttpResponseRedirect('/projeto_perfil/%s' % str(projeto.id))

    lista_projetos = Projeto.objects.all()

    return render(request, 'projeto_cadastrar.html', locals())


def projeto_editar(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    novo_projeto = ProjetoForm(instance=projeto)

    if request.method == 'POST':
        novo_projeto = ProjetoForm(request.POST, instance=projeto)
        if novo_projeto.is_valid():
            projeto = novo_projeto.save()
            return HttpResponseRedirect('/projeto_perfil/%s' % str(projeto.id))

    lista_projetos = Projeto.objects.all()

    return render(request, 'projeto_cadastrar.html', locals())


def projeto_perfil(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    nome_projeto = projeto.nome

    return render(request, 'projeto_perfil.html', locals())


def projeto_deletar(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()

    return HttpResponseRedirect("/home/")


def cadastra_usuario(request):
    cadastro = True
    membro_form = MembroForm()
    if request.method == 'POST':
        login = request.POST['login']
        senha = request.POST['senha']
        confirmacao_senha = request.POST['confirmacao_senha']
        numero_usuario = User.objects.filter(username__iexact = login).count()
        if numero_usuario == 0:
            if confirmacao_senha == senha:
                membro_form = MembroForm(request.POST)
                if membro_form.is_valid():
                    user = User.objects.create_user(login, confirmacao_senha, senha)
                    user.save()
                    membro = membro_form.save(commit = False)
                    membro.usuario = user
                    membro.save()
                    return HttpResponse('<script>alert("Usuário cadastrado com sucesso"); history.back()</script>')
            else:
                return HttpResponse('<script>alert("Senhas não coincidem"); history.back()</script>')
        else:
            return HttpResponse('<script>alert("Login já existente"); history.back()</script>')
    return render(request, 'cadastra_usuario.html', locals())

def atualiza_usuario(request, usuario_id):
    membro = Membro.objects.get(id = usuario_id)
    membro_form = MembroForm(instance = membro)
    if request.method == 'POST':
        membro_form = MembroForm(request.POST, instance=membro)
        if membro_form.is_valid():
            membro_form.save()
            return HttpResponse('<script>alert("Usuário atualizado com sucesso"); history.back()</script>')
    return render(request, 'cadastra_usuario.html', locals())

def deleta_usuario(request, usuario_id):
    membro = Membro.objects.get(id = usuario_id)
    user = membro.usuario
    membro.delete()
    user.delete()
    return HttpResponse('<script>alert("O usuário foi deletado"); history.back()</script>')

def perfil_usuario(request, usuario_id):
    membro = Membro.objects.get(id = usuario_id)
    try:
        lista_cargos = Cargo.objects.filter(membro=membro)
    except:
        lista_cargos = False
    return render(request, 'perfil_usuario.html', locals())

def lista_usuario(request):
    lista_usuario = Membro.objects.all()
    lista_usuario_e_projeto = []
    for usuario in lista_usuario:
        lista_usuario_e_projeto.append([usuario, Cargo.objects.filter(membro=usuario)])
    return render(request, 'lista_usuario.html', locals())


def cadastrar_nucleo(request):
    nucleo_form = NucleoForm()
    if request.method == "POST":
        nucleo_form = NucleoForm(request.POST)
        if nucleo_form.is_valid():
            nucleo_form.save()
            return HttpResponse('<script>alert("Núcleo cadastrado com sucesso"); location.replace("/cadastrar_nucleo/")</script>')

    texto = "Cadastro de um novo núcleo"
    return render(request, 'cadastrar_nucleo.html', locals())

def atualizar_nucleo(request, nucleo_id):
    nucleo = Nucleo.objects.get(id = nucleo_id)
    nucleo_form = NucleoForm(instance = nucleo)
    if request.method == "POST":
        nucleo_form = NucleoForm(request.POST, instance = nucleo)
        if nucleo_form.is_valid():
            nucleo_form.save()
            return HttpResponse('<script>alert("Núcleo atualizado com sucesso"); location.replace("/ver_nucleos/")</script>')

    texto = "Atualizar núcleo"
    return render(request, 'cadastrar_nucleo.html', locals())

def apagar_nucleo(requst, nucleo_id):
    nucleo = Nucleo.objects.get(id = nucleo_id)
    nucleo.delete()
    return HttpResponse('<script>location.replace("/ver_nucleos/")</script>')

def ver_nucleos(request):
    lista_nucleo = Nucleo.objects.all()
    return render(request, 'ver_nucleos.html', locals())


def cadastra_cargo(request, usuario_id):
    membro = Membro.objects.get(id=usuario_id)
    cargo_form = CargoForm()
    if request.method == 'POST':
        cargo_form = CargoForm(request.POST)
        if cargo_form.is_valid():
            cargo = cargo_form.save(commit = False)
            cargo.membro = membro
            cargo.save()
            return HttpResponse('<script>alert("Cargo cadastrado com sucesso"); history.back()</script>')
    return render(request, 'cadastra_cargo.html', locals())

