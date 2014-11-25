# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acesso', '0002_auto_20141124_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='acesso',
            name='Nomep',
            field=models.ForeignKey(verbose_name=b'Local', to='acesso.Local', null=True),
            preserve_default=True,
        ),
    ]
