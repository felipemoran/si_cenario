# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membro',
            name='nucleo',
        ),
        migrations.RemoveField(
            model_name='membro',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Nucleo',
        ),
        migrations.RenameField(
            model_name='projeto',
            old_name='data_inicio',
            new_name='data_de_inicio',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='membro',
        ),
        migrations.DeleteModel(
            name='Membro',
        ),
        migrations.AlterField(
            model_name='projeto',
            name='etapa',
            field=models.CharField(max_length=50, verbose_name=b'Etapa', choices=[(b'analise_tecnica', b'Analise Tecnica'), (b'finalizado', b'Finalizado'), (b'planejamento', b'Planejamento'), (b'execucao', b'Execucao'), (b'suporte_tecnico', b'Suporte Tecnico')]),
            preserve_default=True,
        ),
    ]
