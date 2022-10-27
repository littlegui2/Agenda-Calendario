from email.policy import default
from enum import unique
from tabnanny import verbose
from tokenize import Number, blank_re
from xml.etree.ElementInclude import default_loader
from django.db import models
from django.forms import CharField, DateField, IntegerField
from phonenumber_field.modelfields import PhoneNumberField
from accounts.models.user import User
#criação do relatorio 
#criaçao do template da equipe
#salvar como csv 
#lista de relatorios 
#atribuir permissões 
class Equipe(models.Model):
    nome = models.CharField('Digite o nome da equipe', max_length=32, unique = True)
    codigoV = models.CharField('Digite o codigo do vendedor', max_length=32)
    contato = PhoneNumberField(region="BR",unique = True, null = False, blank = False,  help_text='Insira um número válido.')
    funcionario = models.ManyToManyField(User)
    def __str__(self):
        return self.nome
    
class Relatorio(models.Model):
    STATUS_CHOICE = (
        ("segunda","Segunda-feira"),
        ("terça","Terça-feira"),
        ("quarta","Quarta-feira"),
        ("quinta","Quinta-feira"),
        ("sexta","Sexta-feira"),
        ("sabado","Sabado")
    )
    STATUS_CHOICE1 = (
        ("janeiro","Janeiro"),
        ("fevereiro","Fevereiro"),
        ("marco","Março"),
        ("abril","Abril"),
        ("maio","Maio"),
        ("junho","Junho"),
        ("julho","Julho"),
        ("agosto","Agosto"),
        ("setembro","Setembro"),
        ("outubro","Outubro"),
        ("novembro","Novembro"),
        ("dezembro","Dezembro"),
        
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    codigo = models.IntegerField()
    frequencia = models.IntegerField()
    data = models.CharField(max_length=20, choices=STATUS_CHOICE, blank=False, null=False)
    mes = models.CharField(max_length=10,choices=STATUS_CHOICE1, blank =False, null=False, default='Escolha um mês')

    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
   
    #definir horari que funcionario vai trabalhar
    
    def __str__(self):
       return self.equipeNome,self.mes

  