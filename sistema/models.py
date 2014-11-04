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

CARGO_CHOICE = (
    ('gerente', 'Gerente'),
    ('analista', 'Analista'),
    ('coordenador', 'Coordenador'),
    ('trainee', 'Trainee'),
    )


class Membro(models.Model):
    usuario = models.OneToOneField(User)
    nome = models.CharField("Nome", max_length=64)
    sobrenome = models.CharField("Sobrenome", max_length=64)
    email = models.EmailField(null=False)

    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"

    def __unicode__(self):
        return self.nome + ' ' + self.sobrenome


class Projeto(models.Model):
    nome = models.CharField("Nome", max_length=50)
    data_de_inicio = models.DateField(blank=True, null=True)
    data_de_termino = models.DateField(blank=True, null=True)
    status = models.CharField("Status", max_length=50, choices=STATUS_CHOICE, blank=True, null=True)
    etapa = models.CharField("Etapa", max_length=50, choices=ETAPA_CHOICE, blank=True, null=True)
    membros = models.ManyToManyField(Membro, blank=True, null=True)
    descricao = models.TextField()

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __unicode__(self):
        return self.nome


class Nucleo(models.Model):
    nome = models.CharField("Nome", max_length=32)
    membros = models.ManyToManyField(Membro, through='Cargo')

    class Meta:
        verbose_name = "Nucleo"
        verbose_name_plural = "Nucleos"

    def __unicode__(self):
        return self.nome


class Cargo(models.Model):
    cargo = models.CharField("Cargo", choices=CARGO_CHOICE, max_length=50)
    membro = models.ForeignKey(Membro)
    nucleo = models.ForeignKey(Nucleo)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __unicode__(self):
        return self.membro.nome + ' - ' + self.nucleo.nome


