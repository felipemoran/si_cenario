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

@login_required
def home(request):
    return HttpResponseRedirect('/perfil_usuario/%s' %request.user.membro.id)


def teste(request):
    return render(request, 'teste.html', locals())


@login_required
def projeto_lista(request):
    lista_projetos = Projeto.objects.all()

    return render(request, 'projeto_lista.html', locals())

@login_required
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

    lista_gerente = Cargo.objects.filter(projeto = projeto, cargo__iexact = 'gerente')
    if not lista_gerente:
        gerente_erro = 'Não há nenhum gerente alocado para esse projeto'

    analistas = Cargo.objects.filter(projeto = projeto)
    if not analistas:
        analistas_erro = 'Não há nenhum membro alocado para esse projeto'

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
        print "____________________" #arrumar aqui #paulo
        login = request.POST['login']
        print login
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
                    #mudar para os redirecionamentos adequados
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
    lista_cargo = Cargo.objects.filter(membro = membro)
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


def cadastra_cargo2(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    cargo_form = CargoForm2()
    if request.method == 'POST':
        cargo_form = CargoForm2(request.POST)
        if cargo_form.is_valid():
            cargo = cargo_form.save(commit = False)
            cargo.projeto = projeto
            cargo.save()
            return HttpResponse('<script>alert("Cargo cadastrado com sucesso"); location.replace("/projeto_perfil/%s")</script>' %str(projeto.id))
    return render(request, 'cadastra_cargo.html', locals())


def deleta_cargo(request, cargo_id):
    cargo = Cargo.objects.get(id=cargo_id)
    cargo.delete()
    return HttpResponse('<script>history.go(-1)</script>')



#Paulo
# def login_fazer(request):
#     if request.method == 'GET':
#         login_form = LoginForm()
#     else:
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             login = login_form.cleaned_data['login']
#             senha = login_form.cleaned_data['senha']
#             user = authenticate(username=login, password=senha)
#             if user is not None:
#                 if user.is_active:
#                     login(request,user)
#                     request.session.set_expiry(0) #nao sei o que essa linha faz
#                     return redirect('/cadastra_usuario') #aqui, na realidade, deveria redirecionar para o perfil do usuário logado mas preciso saber como pegar no banco o id do usuário que logou
#                 else:
#                     messages.warning(request, _(u'Usuário inativo.'))
#             else:
#                 messages.warning(request, _(u'Tente outro usuário e/ou senha.'))
#         else:
#             messages.warning(request, _('Preencha os campos corretamente.'))
#     return render('login_fazer.html', locals(), context_instance=RequestContext(request))

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
                    return HttpResponse('<script>alert("Usuário logado!"); location.replace("/perfil_usuario/%s")</script>' %str(user.membro.id))
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
    return HttpResponse('<script>alert("Logout efetuado!"); location.request("/login_fazer/")</script>')


