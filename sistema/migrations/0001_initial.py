# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=64, verbose_name=b'Nome')),
                ('sobrenome', models.CharField(max_length=64, verbose_name=b'Sobrenome')),
                ('email', models.EmailField(max_length=75)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Membro',
                'verbose_name_plural': 'Membros',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, verbose_name=b'Nome')),
                ('data_de_inicio', models.DateField()),
                ('status', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Status', choices=[(b'em_dia', b'Em dia'), (b'atrasado', b'Atrasado')])),
                ('etapa', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Etapa', choices=[(b'analise_tecnica', b'Analise Tecnica'), (b'finalizado', b'Finalizado'), (b'planejamento', b'Planejamento'), (b'execucao', b'Execucao'), (b'suporte_tecnico', b'Suporte Tecnico')])),
                ('descricao', models.TextField()),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
            },
            bases=(models.Model,),
        ),
    ]
