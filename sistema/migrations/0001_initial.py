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
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cargo', models.CharField(max_length=50, verbose_name=b'Cargo', choices=[(b'gerente', b'Gerente'), (b'analista', b'Analista'), (b'coordenador', b'Coordenador'), (b'trainee', b'Trainee')])),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=64, verbose_name=b'Nome')),
                ('sobrenome', models.CharField(max_length=64, verbose_name=b'Sobrenome')),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Membro',
                'verbose_name_plural': 'Membros',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nucleo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=32, verbose_name=b'Nome')),
                ('membros', models.ManyToManyField(to='sistema.Membro', through='sistema.Cargo')),
            ],
            options={
                'verbose_name': 'Nucleo',
                'verbose_name_plural': 'Nucleos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, verbose_name=b'Nome')),
                ('data_de_inicio', models.DateField(verbose_name=b'Data de in\xc3\xadcio')),
                ('status', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Status', choices=[(b'Em dia', b'Em dia'), (b'Atrasado', b'Atrasado')])),
                ('etapa', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Etapa', choices=[(b'Analise Tecnica', b'An\xc3\xa1lise T\xc3\xa9cnica'), (b'Planejamento', b'Planejamento'), (b'Execucao', b'Execu\xc3\xa7\xc3\xa3o'), (b'Suporte Tecnico', b'Suporte T\xc3\xa9cnico'), (b'Finalizado', b'Finalizado')])),
                ('descricao', models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cargo',
            name='membro',
            field=models.ForeignKey(to='sistema.Membro'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cargo',
            name='nucleo',
            field=models.ForeignKey(to='sistema.Nucleo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cargo',
            name='projeto',
            field=models.ForeignKey(blank=True, to='sistema.Projeto', null=True),
            preserve_default=True,
        ),
    ]
