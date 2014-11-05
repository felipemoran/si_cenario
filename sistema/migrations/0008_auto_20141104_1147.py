# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0007_auto_20141104_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='email',
            field=models.EmailField(unique=True, max_length=75),
            preserve_default=True,
        ),
    ]
