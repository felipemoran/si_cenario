# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0004_remove_membro_nucleo'),
    ]

    operations = [
        migrations.AddField(
            model_name='membro',
            name='nucleo',
            field=models.ForeignKey(blank=True, to='sistema.Nucleo', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membro',
            name='email',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membro',
            name='login',
            field=models.CharField(max_length=64, verbose_name=b'Login'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membro',
            name='nome',
            field=models.CharField(max_length=64, verbose_name=b'Nome'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membro',
            name='password',
            field=models.CharField(max_length=64, verbose_name=b'Password'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membro',
            name='sobrenome',
            field=models.CharField(max_length=64, verbose_name=b'Sobrenome'),
            preserve_default=True,
        ),
    ]
