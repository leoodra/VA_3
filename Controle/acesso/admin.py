#coding:utf-8
from django.contrib import admin
from models import Pessoa
from models import Local
from models import Acesso

# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Local)
admin.site.register(Acesso)


