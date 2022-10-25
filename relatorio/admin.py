from django.contrib import admin
from .models import Relatorio, Equipe
# Register your models here.

class RelatorioAdmin(admin.ModelAdmin):
    list_display = ('equipeNome','codigo', 'frequencia','data','mes','data_criacao')
     
    search_fields = ("mes",)


admin.site.register(Relatorio,RelatorioAdmin)
admin.site.register(Equipe)