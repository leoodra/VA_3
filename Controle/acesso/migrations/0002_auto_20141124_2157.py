# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acesso', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='TipoAcesoP',
            new_name='TipoAcessoP',
        ),
    ]
