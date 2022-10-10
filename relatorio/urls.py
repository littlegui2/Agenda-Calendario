from django.contrib import admin
from django.urls import path, include

from relatorio.models import Equipe

from .views import RelatorioCad, RelatorioListagem, EquipeCad, EquipeListagem

app_name = 'relatorio'

urlpatterns = [
    path("relatorio/", RelatorioCad.as_view(), name="relatorio"),
    path("relatorios/", RelatorioListagem.as_view(), name="relatorios"),
    path("equipe/", EquipeCad.as_view(), name="equipe"),
    path("equipes/", EquipeListagem.as_view(), name="equipes"),

    
]
