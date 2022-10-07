from enum import unique
from tokenize import Number
from django.db import models
from django.forms import CharField, DateField, IntegerField

class Relatorio(models.Model):
    equipe = models.CharField('Digite o nome da equipe', max_length=32)
    cod_vendedor = models.CharField('Digite o codigo do vendedor', max_length=32)
    nome = models.CharField('Digite seu nome', max_length=32)
    email = models.EmailField('Digite seu email', max_length=32)
    codigo = models.IntegerField()
    frequencia = models.IntegerField()
    data = models.DateField()
    #definir horari que funcionario vai trabalhar
    def __str__(self):
        return self.nome

    # Create your models here.