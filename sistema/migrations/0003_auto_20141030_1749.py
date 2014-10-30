# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_auto_20141030_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(default=b'ERRADO', max_length=64, verbose_name=b'Nome')),
                ('sobrenome', models.CharField(default=b'ERRADO', max_length=64, verbose_name=b'Sobrenome')),
                ('email', models.EmailField(default=b'ERRADO', max_length=75)),
                ('login', models.CharField(default=b'ERRADO', max_length=64, verbose_name=b'Login')),
                ('password', models.CharField(default=b'ERRADO', max_length=64, verbose_name=b'Password')),
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
            ],
            options={
                'verbose_name': 'Nucleo',
                'verbose_name_plural': 'Nucleos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='membro',
            name='nucleo',
            field=models.ForeignKey(blank=True, to='sistema.Nucleo', null=True),
            preserve_default=True,
        ),
    ]
