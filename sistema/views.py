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
def projeto_cadastrar(request):
    membro = request.user.membro
    projeto = Projeto.objects.all()
    cargo = Cargo.objects.filter(projeto = projeto, cargo__iexact = 'coordenador')
    if cargo:
        novo_projeto = ProjetoForm()
        if request.method == 'POST':
            novo_projeto = ProjetoForm(request.POST)
            print novo_projeto
            if novo_projeto.is_valid():
                projeto = novo_projeto.save(commit=False)
                projeto.save()
                return HttpResponse('<script>alert("Projeto cadastrado com sucesso"); location.replace("/projeto_perfil/%s")</script>' % str(projeto.id))
    else:
        return HttpResponse('<script>alert("Você não tem permissão para cadastrar um projeto."); history.back()</script>')

    lista_projetos = Projeto.objects.all()

    return render(request, 'projeto_cadastrar.html', locals())

@login_required
def projeto_lista(request):
    lista_projetos = Projeto.objects.all()
    lista_geral = []

    for projeto in lista_projetos:
        gerente_lista = Cargo.objects.filter(projeto = projeto, cargo__iexact = 'gerente')
        if len(gerente_lista) > 0:
            gerente = Cargo.objects.get(projeto = projeto, cargo__iexact = 'gerente')
            lista_geral.append([projeto, gerente.membro.nome + ' ' + gerente.membro.sobrenome, gerente.nucleo.nome])
        else:
            lista_geral.append([projeto, 'Gerente não detectado.', 'Núcleo não detectado.'])
    return render(request, 'projeto_lista.html', locals())

@login_required
def projeto_editar(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    novo_projeto = ProjetoForm(instance=projeto)
    membro = request.user.membro
    projeto2 = Projeto.objects.all()
    cargo = Cargo.objects.filter(projeto = projeto2, cargo__iexact = 'coordenador')
    if cargo:
        if request.method == 'POST':
            novo_projeto = ProjetoForm(request.POST, instance=projeto)
            if novo_projeto.is_valid():
                projeto = novo_projeto.save()
                return HttpResponse('''
                    <script>alert("Projeto editado com sucesso");
                    location.replace("/projeto_perfil/%s")
                    </script>''' % str(projeto.id))
        else:
            return HttpResponse('<script>alert("Você não tem permissão para editar um projeto."); history.back()</script>')

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
    membro = request.user.membro
    projeto = Projeto.objects.all()
    cargo = Cargo.objects.filter(projeto = projeto, cargo__iexact = 'coordenador')
    if cargo:
        projeto = Projeto.objects.get(id=projeto_id)
        projeto.delete()
        return HttpResponse('<script>alert("Projeto deletado com sucesso"); location.replace("/projeto_lista/")</script>')
    else:
        return HttpResponse('<script>alert("Você não tem permissão para cadastrar um projeto."); history.back()</script>')


def cadastra_usuario(request):
    cadastro = True
    membro_form = MembroForm()
    coordenador = False
    if Cargo.objects.filter(cargo = 'coordenador', id = request.user.membro.id):
        coordenador = True
    if coordenador:
        if request.method == 'POST':
            login = request.POST['login']
            senha = request.POST['senha']
            confirmacao_senha = request.POST['confirmacao_senha']
            numero_usuario = User.objects.filter(username__iexact = login).count()
            if numero_usuario == 0:
                if len(login)>=5:
                    if confirmacao_senha == senha and len(confirmacao_senha)>=5:
                        membro_form = MembroForm(request.POST)
                        if membro_form.is_valid():
                            user = User.objects.create_user(login, confirmacao_senha, senha)
                            user.save()
                            membro = membro_form.save(commit = False)
                            membro.usuario = user
                            membro.save()
                            return HttpResponse('<script>alert("Usuário cadastrado com sucesso."); history.back()</script>')
                    else:
                        return HttpResponse('<script>alert("As senhas devem coincidir. Mínimo 5 caracteres."); history.back()</script>')
                return HttpResponse('<script>alert("Digite um login válido. Mínimo 5 caracteres."); history.back()</script>')
            else:
                return HttpResponse('<script>alert("Login já existente."); history.back()</script>')
    else:
        return HttpResponse('<script>alert("Você não tem permissao para essa operação."); location.replace("/home/")</script>')
    return render(request, 'home.html', locals())

@login_required
def atualiza_usuario(request, usuario_id):
    atualizar = True
    lista_cargos = Cargo.objects.filter(cargo = 'coordenador', id = request.user.membro.id)
    if (int(usuario_id) == int(request.user.membro.id)) or lista_cargos:
        membro = Membro.objects.get(id = usuario_id)
        membro_form = MembroForm(instance = membro)
        if request.method == 'POST':
            membro_form = MembroForm(request.POST, instance=membro)
            if membro_form.is_valid():
                membro_form.save()
                return HttpResponse('<script>alert("Usuário atualizado com sucesso."); history.back()</script>')
    else:
        return HttpResponse('<script>alert("Você não tem permissao para essa operação."); location.replace("/home/")</script>')
    return render(request, 'cadastra_usuario.html', locals())

@login_required
def deleta_usuario(request, usuario_id):
    coordenador = False
    if Cargo.objects.filter(cargo = 'coordenador', id = request.user.membro.id):
        coordenador = True
    if coordenador:
        membro = Membro.objects.get(id = usuario_id)
        user = membro.usuario
        membro.delete()
        user.delete()
        return HttpResponse('<script>alert("O usuário foi deletado com sucesso."); location.replace(/home/)</script>')
    else:
        return HttpResponse('<script>alert("Você não tem permissao para essa operação."); location.replace("/home/")</script>')

@login_required
def perfil_usuario(request, usuario_id):
    coordenador = False
    projetos_atuais = Cargo.objects.filter()
    if Cargo.objects.filter(cargo = 'coordenador', id = request.user.membro.id):
        coordenador = True
    try:
       membro = Membro.objects.get(id = usuario_id)
    except:
        return HttpResponse('<script>alert("Usuário inexistente."); location.replace(/home/)</script>')
    lista_cargo = Cargo.objects.filter(membro = membro)
    try:
        lista_cargos = Cargo.objects.filter(membro=membro)
    except:
        lista_cargos = False
    return render(request, 'perfil_usuario.html', locals())


def lista_usuario(request):
    id_atual = request.user.membro.id
    coordenador = False
    if Cargo.objects.filter(cargo = 'coordenador', id = request.user.membro.id):
        coordenador = True
    lista_usuario = Membro.objects.all()
    lista_usuario_e_projeto = []
    for usuario in lista_usuario:
        lista_usuario_e_projeto.append([usuario, Cargo.objects.filter(membro=usuario)])

    '''
    #Solucao possivel mas ainda nao funciona
    lista_nucleos = []
    for elemento in lista_usuario_e_projeto:
        for cargo in elemento[1]:
            if not(cargo.nucleo.nome in lista_nucleos):
                lista_nucleos.append(cargo.nucleo.nome)
    '''

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

def apagar_nucleo(request, nucleo_id):
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
    membro = request.user.membro
    projeto = Projeto.objects.get(id=projeto_id)
    projeto2 = Projeto.objects.all()
    cargo_form = CargoForm2()
    cargo = Cargo.objects.filter(projeto = projeto2, cargo__iexact = 'coordenador')
    if cargo:
        if request.method == 'POST':
            cargo_form = CargoForm2(request.POST)
            if cargo_form.is_valid():
                cargo = cargo_form.save(commit = False)
                cargo.projeto = projeto
                cargo.save()
                return HttpResponse('<script>alert("Membro adicionado com sucesso"); location.replace("/projeto_perfil/%s")</script>' %str(projeto.id))
    else:
        return HttpResponse('<script>alert("Você não tem permissão para adicionar um membro."); history.back()</script>')
    return render(request, 'cadastra_cargo.html', locals())


def deleta_cargo(request, cargo_id):
    cargo = Cargo.objects.get(id=cargo_id)
    cargo.delete()
    return HttpResponse('<script>history.go(-1)</script>')

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


