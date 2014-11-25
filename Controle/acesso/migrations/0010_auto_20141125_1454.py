# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acesso', '0009_auto_20141125_1414'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='acesso',
            unique_together=None,
        ),
    ]
