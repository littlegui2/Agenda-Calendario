from django import views
from django.contrib import admin
from django.urls import path, include

from relatorio.models import Equipe

from relatorio.views import EquipeDelete, EquipeUpdate, Impview, RelatorioCad, listaFuncionario, relatorioLista, EquipeCad, relatorios_d, equipeLista, RelatorioUpdate,RelatorioDelete,pagina_principal,venue_csv

app_name = 'relatorio'

urlpatterns = [
    path("relatorio/", RelatorioCad.as_view() , name="relatorio"),
    path("relatorios/", relatorioLista, name="relatorios"),
    path("equipe/", EquipeCad.as_view(), name="equipe"),
    path('relatorios/<str:chave>/<str:x>', relatorios_d, name="info" ),
    path("equipes/",equipeLista, name="equipes"),
    path('equipes-udpate/<int:pk>/', EquipeUpdate.as_view(), name="equipe-up"),
    path('equipes-delete/<int:pk>/', EquipeDelete.as_view(), name="equipe-del"),
    path('relatorios-udpate/<int:pk>/', RelatorioUpdate.as_view(), name="relatorio-up"),
    path('relatrorios-delete/<int:pk>/', RelatorioDelete.as_view(), name="relatorio-del"),
    path('', pagina_principal, name='pagina-principal' ),
    path('funcionarios/', listaFuncionario, name="funcionarios" ),
    path('imprimir/', Impview.as_view(), name='imprimir' ),
    path('venue_csv/', venue_csv , name='venue_csv'),
]

