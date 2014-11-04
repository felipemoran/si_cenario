# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sistema', '0005_auto_20141030_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cargo', models.CharField(max_length=50, verbose_name=b'Cargo', choices=[(b'gerente', b'Gerente'), (b'analista', b'Analista'), (b'coordenador', b'Coordenador'), (b'trainee', b'Trainee')])),
                ('membro', models.ForeignKey(to='sistema.Membro')),
                ('nucleo', models.ForeignKey(to='sistema.Nucleo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='membro',
            name='login',
        ),
        migrations.RemoveField(
            model_name='membro',
            name='nucleo',
        ),
        migrations.RemoveField(
            model_name='membro',
            name='password',
        ),
        migrations.AddField(
            model_name='membro',
            name='usuario',
            field=models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nucleo',
            name='membros',
            field=models.ManyToManyField(to='sistema.Membro', through='sistema.Cargo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nucleo',
            name='nome',
            field=models.CharField(default='nucleo', max_length=32, verbose_name=b'Nome'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projeto',
            name='data_de_termino',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projeto',
            name='membros',
            field=models.ManyToManyField(to='sistema.Membro'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projeto',
            name='data_de_inicio',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projeto',
            name='etapa',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Etapa', choices=[(b'analise_tecnica', b'Analise Tecnica'), (b'finalizado', b'Finalizado'), (b'planejamento', b'Planejamento'), (b'execucao', b'Execucao'), (b'suporte_tecnico', b'Suporte Tecnico')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projeto',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Status', choices=[(b'em_dia', b'Em dia'), (b'atrasado', b'Atrasado')]),
            preserve_default=True,
        ),
    ]
