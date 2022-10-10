from enum import unique
from tabnanny import verbose
from tokenize import Number
from django.db import models
from django.forms import CharField, DateField, IntegerField
from phonenumber_field.modelfields import PhoneNumberField
#criação do relatorio 
#criaçao do template da equipe
#salvar como csv 
#lista de relatorios 
#atribuir permissões 
class Equipe(models.Model):
    equipe = models.CharField('Digite o nome da equipe', max_length=32)
    cod_vendedor = models.CharField('Digite o codigo do vendedor', max_length=32)
    contato = models.IntegerField(verbose_name="Contato")
    
    def __str__(self) -> str:
        return self.equipe
    
class Relatorio(models.Model):
    STATUS_CHOICE = (
        ("segunda","segunda"),
        ("terça","terça"),
        ("quarta","quarta"),
        ("quinta","quinta"),
        ("sexta","sexta"),
    )
    equipename = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    nome = models.CharField('Digite seu nome', max_length=32)
    email = models.EmailField('Digite seu email', max_length=32)
    codigo = models.IntegerField()
    frequencia = models.IntegerField()
    data = models.CharField(max_length=20, choices=STATUS_CHOICE, blank=False, null=False)
    mes = models.CharField(max_length=10)
    #definir horari que funcionario vai trabalhar
    def __str__(self):
        return self.nome

    # Create your models here.