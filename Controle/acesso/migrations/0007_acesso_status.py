# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acesso', '0006_auto_20141125_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='acesso',
            name='Status',
            field=models.BooleanField(default=False, verbose_name=b'Acessando'),
            preserve_default=True,
        ),
    ]
