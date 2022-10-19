from django import views
from django.contrib import admin
from django.urls import path, include

from relatorio.models import Equipe

from relatorio.views import Impview, RelatorioCad, relatorioLista, EquipeCad, relatorios_d, RelatorioInfo, equipeLista, RelatorioUpdate,RelatorioDelete,pagina_principal, venue_pdf,venue_csv, venue_text

app_name = 'relatorio'

urlpatterns = [
    path("relatorio/", RelatorioCad.as_view(), name="relatorio"),
    path("relatorios/", relatorioLista, name="relatorios"),
    path("equipe/", EquipeCad.as_view(), name="equipe"),
    path('relatorios/<str:chave>/', relatorios_d, name="info" ),
    path("equipes/",equipeLista, name="equipes"),
    path('relatorios-udpate/<int:pk>/', RelatorioUpdate.as_view(), name="relatorio-up"),
    path('relatrorios-delete/<int:pk>/', RelatorioDelete.as_view(), name="relatorio-del"),
    path('', pagina_principal, name='pagina-principal' ),
    path('imprimir/', Impview.as_view(), name='imprimir' ),
    path('venue_csv/', venue_csv , name='venue_csv'),
    path('venue_text/', venue_text , name='venue_text'),
    path('venue_pdf/', venue_pdf , name='venue_pdf')
]
