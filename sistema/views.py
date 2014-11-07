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
    lista_projetos = Projeto.objects.all()

    return render(request, 'projeto_lista.html', locals())

@login_required
def projeto_cadastrar(request):
    novo_projeto = ProjetoForm()
    if request.method == 'POST':
        novo_projeto = ProjetoForm(request.POST)
        if novo_projeto.is_valid():
            projeto = novo_projeto.save(commit=False)
            projeto.save()
            return HttpResponseRedirect('/projeto_perfil/%s' % str(projeto.id))

    lista_projetos = Projeto.objects.all()

    return render(request, 'projeto_cadastrar.html', locals())

@login_required
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

@login_required
def projeto_perfil(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    nome_projeto = projeto.nome

    return render(request, 'projeto_perfil.html', locals())

@login_required
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

@login_required
def atualiza_usuario(request, usuario_id):
    membro = Membro.objects.get(id = usuario_id)
    membro_form = MembroForm(instance = membro)
    if request.method == 'POST':
        membro_form = MembroForm(request.POST, instance=membro)
        if membro_form.is_valid():
            membro_form.save()
            return HttpResponse('<script>alert("Usuário atualizado com sucesso"); history.back()</script>')
    return render(request, 'cadastra_usuario.html', locals())

@login_required
def deleta_usuario(request, usuario_id):
    membro = Membro.objects.get(id = usuario_id)
    user = membro.usuario
    membro.delete()
    user.delete()
    return HttpResponse('<script>alert("O usuário foi deletado"); history.back()</script>')

@login_required
def perfil_usuario(request, usuario_id):
    membro = Membro.objects.get(id = usuario_id)
    return render(request, 'perfil_usuario.html', locals())

#Paulo
'''
def login_fazer(request):
    if request.method == 'GET':
        login_form = LoginForm()
    else:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login = login_form.cleaned_data['login']
            senha = login_form.cleaned_data['senha']
            user = authenticate(username=login, password=senha)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    request.session.set_expiry(0) #nao sei o que essa linha faz
                    return redirect('/cadastra_usuario') #aqui, na realidade, deveria redirecionar para o perfil do usuário logado mas preciso saber como pegar no banco o id do usuário que logou
                else:
                    messages.warning(request, _(u'Usuário inativo.'))
            else:
                messages.warning(request, _(u'Tente outro usuário e/ou senha.'))
        else:
            messages.warning(request, _('Preencha os campos corretamente.'))
    return render('login_fazer.html', locals(), context_instance=RequestContext(request))
    '''

def login_fazer(request):
    if request.method == 'GET':
        login_form = LoginForm()
    else:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST['login']
            password = request.POST['senha']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('<script>alert("Usuário logado!"); history.back()</script>')
                    #return redirect('/cadastra_usuario')# Redirect to a success page.
                else:
                    return HttpResponse('<script>alert("Usuário inativo!"); history.back()</script>')
            else:
                return HttpResponse('<script>alert("Usuário e/ou senha incorretos!"); history.back()</script>')
        else:
            messages.warning(request, _('Preencha os campos corretamente.'))
    return render(request, 'login_fazer.html', locals())

@login_required
def logout_fazer(request):
    logout(request)
    return HttpResponse('<script>alert("Logout efetuado!"); history.back()</script>')

