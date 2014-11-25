# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acesso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Hora_EntradaAcess', models.TimeField(auto_now=True, verbose_name=b'Hora de Entrada')),
                ('Hora_SaidaAcesso', models.TimeField(verbose_name=b'Hora da Sa\xc3\xadda')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(unique=True, max_length=57, verbose_name=b'Nome do Local')),
                ('Desc_Local', models.CharField(max_length=77, verbose_name=b'Descri\xc3\xa7\xc3\xa3o do Local')),
                ('TipoAcessoL', models.CharField(max_length=9, verbose_name=b'Tipo de Acesso do Local', choices=[(b'Livre', b'Livre'), (b'Restrito', b'Restrito'), (b'Reservado', b'Reservado')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(unique=True, max_length=37, verbose_name=b'Nome')),
                ('Sexo', models.CharField(max_length=1, verbose_name=b'Sexo', choices=[(b'F', b'Feminino'), (b'M', b'Masculino')])),
                ('TipoAcesoP', models.CharField(max_length=9, verbose_name=b'Tipo de Acesso', choices=[(b'Livre', b'Livre'), (b'Restrito', b'Restrito'), (b'Reservado', b'Reservado')])),
                ('CPF', models.CharField(unique=True, max_length=11, verbose_name=b'CPF')),
                ('DtNas', models.DateField(null=True, verbose_name=b'Data Nascimento')),
                ('Telefone', models.CharField(max_length=13, null=True, verbose_name=b'Telefone')),
                ('Email', models.EmailField(max_length=100, null=True, verbose_name=b'E-mail')),
                ('Cidade', models.CharField(max_length=30, null=True, verbose_name=b'Cidade')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
