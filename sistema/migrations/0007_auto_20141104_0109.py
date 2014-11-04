# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0006_auto_20141104_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='membros',
            field=models.ManyToManyField(to='sistema.Membro', null=True, blank=True),
            preserve_default=True,
        ),
    ]
