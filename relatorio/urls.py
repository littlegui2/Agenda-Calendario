from django.contrib import admin
from django.urls import path, include

from .views import RelatorioCad, RelatorioListagem

app_name = 'relatorio'

urlpatterns = [
    path("relatorio/", RelatorioCad.as_view(), name="relatorio"),
    path("relatorios/", RelatorioListagem.as_view(), name="relatorios"),

    
]
