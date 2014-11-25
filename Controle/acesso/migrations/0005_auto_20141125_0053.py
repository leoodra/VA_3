# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acesso', '0004_auto_20141125_0008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acesso',
            old_name='Nomel',
            new_name='Nome',
        ),
    ]
