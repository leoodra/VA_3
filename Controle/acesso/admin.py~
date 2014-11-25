#coding:utf-8
from django.contrib import admin
from models import Pessoa
from models import Local
from models import Acesso

# Register your models here.

class AcessoAdmin(admin.ModelAdmin):
	list_display = ['Pessoa','Local','Hora_EntradaAcess','Hora_SaidaAcesso','Status','Statuso']
	

admin.site.register(Pessoa)
admin.site.register(Local)
admin.site.register(Acesso,AcessoAdmin)


