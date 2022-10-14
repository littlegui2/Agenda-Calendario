from enum import unique
from tabnanny import verbose
from tokenize import Number, blank_re
from django.db import models
from django.forms import CharField, DateField, IntegerField
from phonenumber_field.modelfields import PhoneNumberField
#criação do relatorio 
#criaçao do template da equipe
#salvar como csv 
#lista de relatorios 
#atribuir permissões 
class Equipe(models.Model):
    nome = models.CharField('Digite o nome da equipe', max_length=32)
    codigoV = models.CharField('Digite o codigo do vendedor', max_length=32)
    contato = models.IntegerField(verbose_name="Contato")
    
    def __str__(self) -> str:
        return self.nome
    
class Relatorio(models.Model):
    STATUS_CHOICE = (
        ("segunda","segunda"),
        ("terça","terça"),
        ("quarta","quarta"),
        ("quinta","quinta"),
        ("sexta","sexta"),
    )
    equipe = models.ForeignKey(Equipe,verbose_name="Nome da Equipe", on_delete=models.CASCADE, null=True, default=0)
    nome = models.CharField('Digite seu nome', max_length=32)
    email = models.EmailField('Digite seu email', max_length=32)
    codigo = models.IntegerField()
    frequencia = models.IntegerField()
    data = models.CharField(max_length=20, choices=STATUS_CHOICE, blank=False, null=False)
    mes = models.CharField(max_length=10, blank =False, null=False, default='')
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    #definir horari que funcionario vai trabalhar
    def __str__(self):
        return self.nome

    # Create your models here.