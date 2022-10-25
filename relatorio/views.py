import io
from multiprocessing import context, get_context
from pipes import Template
from re import template
from urllib import response
from webbrowser import get
from django.forms import ModelForm
from django.http import FileResponse, Http404, JsonResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Equipe, Relatorio
import datetime
from django.http import HttpResponse
import csv



class RelatorioCad(CreateView):
    model = Relatorio
    fields = "__all__"
    template_name = 'cadastroRelatorio.html'
    success_url = reverse_lazy('relatorio:relatorios')

    
def relatorioLista(request):
    
   # relatorios = Relatorio.objects.order_by('data_criacao')
    equipes = Equipe.objects.all()
    total_equipe = equipes.count()
    txt = request.GET.get('mes')
    relatorios = Relatorio.objects.all()
    if txt:
       relatorios = Relatorio.objects.filter(mes__icontains=txt)
    else:
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

class Impview(TemplateView):
    model = Relatorio
    template_name = "imprimir.html"    
    
   
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

    # Generate CSV File Venue List
def venue_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=venues.csv'
	
	# Create a csv writer
	writer = csv.writer(response)

	# Designate The Model
    
	venues = Relatorio.objects.all()

	# Add column headings to the csv file
	writer.writerow(['Equipe Nome', 'Codigo', 'Frequencia', 'Data', 'Mes', 'Data Criação'])

	# Loop Thu and output
	for venue in venues:
		writer.writerow([venue.equipeNome, venue.codigo, venue.frequencia, venue.data, venue.mes, venue.data_criacao])

	return response




 