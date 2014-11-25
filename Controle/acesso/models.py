#coding:utf-8
from django.db import models
from django.core.exceptions import ValidationError

SEXO = [
	('F','Feminino'),
	('M','Masculino')
       ]

ACESSO = [
	  ('Livre','Livre'),
	  ('Restrito','Restrito'),		
	  ('Reservado','Reservado')
         ]


# Create your models here.

class Pessoa(models.Model):
	Nome = models.CharField('Nome',max_length=37,unique=True)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO)
	TipoAcessoP = models.CharField('Tipo de Acesso',max_length=9,choices=ACESSO)
	CPF = models.CharField('CPF',max_length=11,unique=True)
	DtNas = models.DateField('Data Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=13,null=True)
	Email = models.EmailField('E-mail',max_length=100,null=True)
	Cidade = models.CharField('Cidade',max_length=30,null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Nome,self.TipoAcessoP)

class Local(models.Model):
	Nome = models.CharField('Nome do Local',max_length=57,unique = True)
	Desc_Local = models.CharField('Descrição do Local',max_length= 77)	
 	TipoAcessoL = models.CharField('Tipo de Acesso do Local',max_length=9,choices= ACESSO)
	
	def __unicode__(self):
		return "%s - %s" % (self.Nome,self.TipoAcessoL)


class Acesso(models.Model):
	Pessoa = models.ForeignKey(Pessoa,verbose_name="Pessoa",null=True)	
	Local = models.ForeignKey(Local,verbose_name="Local", null=True)
	Hora_EntradaAcess = models.TimeField('Hora de Entrada',auto_now=True)
	Hora_SaidaAcesso = models.TimeField('Hora da Saída')
	Status = models.BooleanField('Acessando',default = False)
	Statuso = models.BooleanField('Saiu',default = False)	

	#def save(self, *args, **kwargs):
	#	q = Acesso.objects.filter(Status=True)
	#	if q:
	#	    raise ValidationError("Pessoa ja esta acessando algum local")
	
	#	super(Acesso,self).save(*args, **kwargs)
	
	class Meta:
		unique_together = ("Status","Pessoa")


	def __unicode__(self):
		return " %s - %s - %s" % (self.Pessoa.Nome,self.Hora_EntradaAcess,self.Hora_SaidaAcesso)

		

