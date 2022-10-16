from django.contrib import admin
from django.urls import path, include

from relatorio.models import Equipe

from relatorio.views import RelatorioCad, relatorioLista, EquipeCad, relatorios_d, RelatorioInfo, equipeLista, RelatorioUpdate,RelatorioDelete,pagina_principal

app_name = 'relatorio'

urlpatterns = [
    path("relatorio/", RelatorioCad.as_view(), name="relatorio"),
    path("relatorios/", relatorioLista, name="relatorios"),
    path("equipe/", EquipeCad.as_view(), name="equipe"),
    path('relatorios/<str:chave>/', relatorios_d, name="info" ),
    path("equipes/",equipeLista, name="equipes"),
    path('relatorios-udpate/<int:pk>/', RelatorioUpdate.as_view(), name="relatorio-up"),
    path('relatrorios-delete/<int:pk>/', RelatorioDelete.as_view(), name="relatorio-del"),
    path('', pagina_principal, name='pagina-principal' )
]
