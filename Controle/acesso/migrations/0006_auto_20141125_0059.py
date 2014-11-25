# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acesso', '0005_auto_20141125_0053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acesso',
            old_name='Nome',
            new_name='Local',
        ),
        migrations.RenameField(
            model_name='acesso',
            old_name='Nomep',
            new_name='Pessoa',
        ),
    ]
