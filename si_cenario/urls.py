# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'si_cenario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'sistema.views.home'),
    url(r'^$', 'sistema.views.home'),
    url(r'^teste/$', 'sistema.views.teste'),

    # URLs de Projeto
    url(r'^projeto_lista/$', 'sistema.views.projeto_lista'),
    url(r'^projeto_cadastrar/$', 'sistema.views.projeto_cadastrar'),
    url(r'^projeto_perfil/(?P<projeto_id>[0-9]+)/$', 'sistema.views.projeto_perfil'),
    url(r'^projeto_editar/(?P<projeto_id>[0-9]+)/$', 'sistema.views.projeto_editar'),
    url(r'^projeto_deletar/(?P<projeto_id>[0-9]+)/$', 'sistema.views.projeto_deletar'),

    # URLs de Usuario
    url(r'^cadastra_usuario/$', 'sistema.views.cadastra_usuario'),
    url(r'^atualiza_usuario/(?P<usuario_id>[0-9]+)/$', 'sistema.views.atualiza_usuario'),
    url(r'^deleta_usuario/(?P<usuario_id>[0-9]+)/$', 'sistema.views.deleta_usuario'),
    url(r'^perfil_usuario/(?P<usuario_id>[0-9]+)/$', 'sistema.views.perfil_usuario'),
    url(r'^lista_usuario/$', 'sistema.views.lista_usuario'),

    #URLs de Nucleo
    url(r'^cadastrar_nucleo/$', 'sistema.views.cadastrar_nucleo'),
    url(r'^atualizar_nucleo/(?P<nucleo_id>[0-9]+)/$', 'sistema.views.atualizar_nucleo'),
    url(r'^apagar_nucleo/(?P<nucleo_id>[0-9]+)/$', 'sistema.views.apagar_nucleo'),
    url(r'^ver_nucleos/$', 'sistema.views.ver_nucleos'),

    #URLs de Cargo
    url(r'^cadastra_cargo/(?P<usuario_id>[0-9]+)/$', 'sistema.views.cadastra_cargo'),



    #URLs de Login/Logout
    url(r'^login_fazer/$', 'sistema.views.login_fazer'),
    url(r'^logout_fazer/$', 'sistema.views.logout_fazer'),
    url(r'^accounts/login/$', 'sistema.views.login_fazer'),

)
