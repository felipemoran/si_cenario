# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0008_auto_20141104_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='projeto',
            field=models.ForeignKey(blank=True, to='sistema.Projeto', null=True),
            preserve_default=True,
        ),
    ]
