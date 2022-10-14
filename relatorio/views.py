from multiprocessing import context, get_context
from webbrowser import get
from django.forms import ModelForm
from django.http import Http404
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Equipe, Relatorio
import datetime

class RelatorioCad(CreateView):
    model = Relatorio
    fields = "__all__"
    template_name = 'cadastroRelatorio.html'
    success_url = reverse_lazy('relatorio:relatorios')

    
def relatorioLista(request):
    
    relatorios = Relatorio.objects.order_by('data_criacao')
    equipes = Equipe.objects.all()
    total_equipe = equipes.count()

    
    context= {'relatorios':relatorios, 'equipes': equipes}
    return render(request, 'listaRelatorio.html', context)

def equipeLista(request):
    equipes = Equipe.objects.all()
    context = {'equipes': equipes}
    return render(request,'equipeLista.html', context )

def relatorios_d (request, chave):
    try: 
        relatorio_info = Relatorio.objects.get(pk=chave)
    except Relatorio.DoesNotExist:
        raise Http404('O relátorio não existe')

    context = {'info': relatorio_info}
    return render(request,'relatorioInfo.html',context)

class RelatorioInfo(DetailView):
    model = Relatorio
    template_name = 'relatorioInfo.html'
    
    def get_context_data(self, **kwargs):
        context = super(RelatorioInfo, self).get_context_data()
        relatorio_obj = self.object
        context['object'] = relatorio_obj
        
        context["info"] = Relatorio.objects.filter(equipe=relatorio_obj)
        return context
    
class RelatorioUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model = Relatorio
    fields = "__all__"
    template_name = 'cadastros/cadastroCliente.html'
    success_url = reverse_lazy('funcionarios:clientes')
    
class EquipeCad(CreateView):
    model = Equipe
    fields = ['nome','codigoV','contato']
    template_name = 'cadastroEquipe.html'
    success_url = reverse_lazy('relatorio:equipes')



class EquipeUpdate(UpdateView):
    modal = Equipe
    template_name = ''