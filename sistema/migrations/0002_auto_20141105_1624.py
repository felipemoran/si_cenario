# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nucleo',
            name='membros',
            field=models.ManyToManyField(to='sistema.Membro', null=True, through='sistema.Cargo'),
            preserve_default=True,
        ),
    ]
