from django.forms import ModelForm
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Equipe, Relatorio
class RelatorioCad(CreateView):
    model = Relatorio
    fields = "__all__"
    template_name = 'cadastroRelatorio.html'
    success_url = reverse_lazy('relatorio:relatorios')
    
class RelatorioListagem(ListView):
    model = Relatorio
    template_name = 'listaRelatorio.html'

class RelatorioUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model = Relatorio
    fields = "__all__"
    template_name = 'cadastros/cadastroCliente.html'
    success_url = reverse_lazy('funcionarios:clientes')
    
class EquipeCad(CreateView):
    model = Equipe
    fields = ['equipe','cod_vendedor','contato']
    template_name = 'cadastroEquipe.html'
    success_url = reverse_lazy('relatorio:equipe')
    
class EquipeListagem(ListView):
    model = Equipe
    template_name = 'listaRelatorio.html'
