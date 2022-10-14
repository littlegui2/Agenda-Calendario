from django.contrib import admin
from django.urls import path, include

from relatorio.models import Equipe

from relatorio.views import RelatorioCad, relatorioLista, EquipeCad, relatorios_d, RelatorioInfo, equipeLista

app_name = 'relatorio'

urlpatterns = [
    path("relatorio/", RelatorioCad.as_view(), name="relatorio"),
    path("relatorios/", relatorioLista, name="relatorios"),
    path("equipe/", EquipeCad.as_view(), name="equipe"),
    path('relatorio/<int:pk>', RelatorioInfo.as_view(), name="info" ),
    path("equipes/",equipeLista, name="equipes")
    
]
