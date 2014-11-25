# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acesso', '0008_acesso_statuso'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='acesso',
            unique_together=set([('Status', 'Pessoa')]),
        ),
    ]
