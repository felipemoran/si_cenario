# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'si_cenario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'sistema.views.home'),
    url(r'^projeto_cadastrar/$', 'sistema.views.projeto_cadastrar'),
    url(r'^projeto_editar/(?P<projeto_id>[0-9]+)/$', 'sistema.views.projeto_editar'),

    url(r'^cadastra_usuario/$','sistema.views.cadastra_usuario')

)
