from multiprocessing import context, get_context
from webbrowser import get
from django.forms import ModelForm
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
    
   # relatorios = Relatorio.objects.order_by('data_criacao')
    equipes = Equipe.objects.all()
    total_equipe = equipes.count()
    relatorios = Relatorio.objects.all()
    
    context= {'relatorios':relatorios, 'equipes': equipes}
    return render(request, 'listaRelatorio.html', context)

def equipeLista(request):
    equipes = Equipe.objects.all()
    context = {'equipes': equipes}
    return render(request,'equipeLista.html', context )

def relatorios_d (request, chave):
    try: 
        equipe = Equipe.objects.get(pk=chave)
    except Relatorio.DoesNotExist:
        raise Http404('O relátorio não existe')
    eq = Equipe.objects.all()
    relatoriox = equipe.relatorio_set.all()
    context = {'info': relatoriox, 'eq': equipe}
    return render(request,'relatorioInfo.html',context)

class RelatorioInfo(DetailView):
    model = Relatorio
    template_name = 'relatorioInfo.html'
    context_object_name = 'relatorios'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        post = Relatorio.objects.get(id=equipe)
        post.update(count=('count') +1)
        return context
    
class RelatorioUpdate(LoginRequiredMixin,UpdateView):
    model = Relatorio
    fields = "__all__"
    template_name = 'cadastroRelatorio.html'
    success_url = reverse_lazy('relatorio:relatorios')

class RelatorioDelete(LoginRequiredMixin,UpdateView):
    model = Relatorio
    success_url = reverse_lazy('relatorio:relatorios')

    
class EquipeCad(CreateView):
    model = Equipe
    fields = ['nome','codigoV','contato']
    template_name = 'cadastroEquipe.html'
    success_url = reverse_lazy('relatorio:equipes')



class EquipeUpdate(UpdateView):
    modal = Equipe
    template_name = ''
    
   
def pagina_principal (request):
    relatorios_total = Relatorio.objects.all().count()
    equipes_total = Equipe.objects.all().count()
    
    context = {'relatorios': relatorios_total, 'equipes': equipes_total}
    return render(request,'pagina_principal.html', context)
   
    
def search_vendor(request, pk):
    data_array = []
    rela = Relatorio.objects.all()
    try:
        player = Relatorio.objects.get(pk=pk)
    except Relatorio.DoesNotExists:
        player = None

    if player:
        data_array.append({
        'fist_name': 'oi',
        'last_name': 'oi',
        'age':'eae'
        })

    return JsonResponse(data_array, safe=False)