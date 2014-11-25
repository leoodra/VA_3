# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acesso', '0007_acesso_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='acesso',
            name='Statuso',
            field=models.BooleanField(default=False, verbose_name=b'Saiu'),
            preserve_default=True,
        ),
    ]
