# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acesso', '0003_acesso_nomep'),
    ]

    operations = [
        migrations.AddField(
            model_name='acesso',
            name='Nomel',
            field=models.ForeignKey(verbose_name=b'Local', to='acesso.Local', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='acesso',
            name='Nomep',
            field=models.ForeignKey(verbose_name=b'Pessoa', to='acesso.Pessoa', null=True),
        ),
    ]
