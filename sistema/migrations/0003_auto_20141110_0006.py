# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_auto_20141105_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='data_de_termino',
            field=models.DateField(null=True, verbose_name=b'Data de in\xc3\xadcio', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membro',
            name='email',
            field=models.EmailField(unique=True, max_length=75, verbose_name=b'Email'),
            preserve_default=True,
        ),
    ]
