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
                ('nome', models.CharField(max_length=50, verbose_name=b'Nome')),
                ('sobrenome', models.CharField(max_length=50, verbose_name=b'Sobrenome')),
                ('coordenador', models.BooleanField(default=False)),
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
                ('nome', models.CharField(max_length=50, verbose_name=b'Nome')),
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
                ('data_inicio', models.DateField()),
                ('status', models.CharField(max_length=50, verbose_name=b'Status', choices=[(b'em_dia', b'Em dia'), (b'atrasado', b'Atrasado')])),
                ('etapa', models.CharField(max_length=50, verbose_name=b'Etapa', choices=[(b'planejamento', b'Planejamento'), (b'execucao', b'Execu\xc3\xa7\xc3\xa3o'), (b'analise_tecnica', b'An\xc3\xa1lise t\xc3\xa9cnica')])),
                ('descricao', models.TextField()),
                ('membro', models.ManyToManyField(to='sistema.Membro')),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='membro',
            name='nucleo',
            field=models.ForeignKey(to='sistema.Nucleo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membro',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
