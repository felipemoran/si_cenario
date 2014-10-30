# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_auto_20141030_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membro',
            name='nucleo',
        ),
    ]
