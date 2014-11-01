# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICE = (
    ("em_dia", "Em dia"),
    ("atrasado", "Atrasado"),
    )

ETAPA_CHOICE = (
    ("analise_tecnica", "Analise Tecnica"),
    ("finalizado", "Finalizado"),
    ("planejamento", "Planejamento"),
    ("execucao", "Execucao"),
    ("suporte_tecnico", "Suporte Tecnico"),
    )


class Projeto(models.Model):
    nome = models.CharField("Nome", max_length=50)
    data_de_inicio = models.DateField()
    status = models.CharField("Status", max_length=50, choices=STATUS_CHOICE, blank=True, null=True)
    etapa = models.CharField("Etapa", max_length=50, choices=ETAPA_CHOICE, blank=True, null=True)
    # membro = models.ManyToManyField(Membro)
    descricao = models.TextField()


    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __unicode__(self):
        return self.nome


# class Nucleo(models.Model):
#     class Meta:
#         verbose_name = "Nucleo"
#         verbose_name_plural = "Nucleos"

#     def __unicode__(self):
#         pass


class Membro(models.Model):
    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"

    nome = models.CharField("Nome", max_length=64)
    sobrenome = models.CharField("Sobrenome", max_length=64)
    email = models.EmailField(null=False)
    #verificar classe de referencia
    nucleo = models.ForeignKey(Nucleo, blank=True, null=True)
    login = models.CharField("Login", max_length=64)
    password = models.CharField("Password", max_length=64)


    def __unicode__(self):
        return self.nome
