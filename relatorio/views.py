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
from django.contrib.auth.decorators import login_required

from accounts.models.user import User
from relatorio.forms import EquipeForm
from .models import Equipe, Relatorio
import datetime
from django.http import HttpResponse
import csv



class RelatorioCad(CreateView, LoginRequiredMixin):
    login_url = '/signup/'
    model = Relatorio
    fields = [ "codigo", "frequencia", "data","mes"]
    template_name = 'cadastroRelatorio.html'
    success_url = reverse_lazy('relatorio:relatorios')
    
    def form_valid(self, form) -> HttpResponse:
        
        form.instance.usuario  =  self.request.user
        
        url=  super().form_valid(form)
        
        return url

    
def relatorioLista(request):
            
   # relatorios = Relatorio.objects.order_by('data_criacao')
    
    if request.user.is_superuser:
        relatorios = Relatorio.objects.all()   
        equipes = Equipe.objects.all()
        context= {'relatorios':relatorios, 'equipes': equipes}
    else: 

        equipes = Equipe.objects.all()
        total_equipe = equipes.count()
        txt = request.GET.get('mes')
        if txt:
            relatorios = Relatorio.objects.filter(usuario = request.user,mes__icontains=txt)
        else:
            relatorios = Relatorio.objects.filter(usuario = request.user)    
        context= {'relatorios':relatorios, 'equipes': equipes}
   

    return render(request, 'listaRelatorio.html', context)
    
     
    

def equipeLista(request):
    equipes = Equipe.objects.all()
    context = {'equipes': equipes}
    return render(request,'equipeLista.html', context )



    
class RelatorioUpdate(LoginRequiredMixin,UpdateView):
    model = Relatorio
    fields = "__all__"
    template_name = 'cadastroRelatorio.html'
    success_url = reverse_lazy('relatorio:relatorios')

class RelatorioDelete(LoginRequiredMixin,DeleteView):
    model = Relatorio
    success_url = reverse_lazy('relatorio:relatorios')
    template_name = 'cadastroRelatorio.html'

def relatorios_d ( request, chave, x ):
    try: 
        user = User.objects.get(pk=request.user.id)
    except Relatorio.DoesNotExist:
        raise Http404('O relátorio não existe')
    eq = Equipe.objects.all()
    
    relatoriox = user.relatorio_set.filter(usuario = request.user,mes=x )
    me = x
    equipe = user.equipe_set.all()
    context = {'info': relatoriox, 'eq': equipe, 'm':me}
    return render(request,'relatorioInfo.html',context)

    
    
class EquipeCad(CreateView):
    model = Equipe
    form_class = EquipeForm
    template_name = 'cadastroEquipe.html'
    success_url = reverse_lazy('relatorio:equipes')
    
    def get_form_kwargs(self):
        
        kwargs = super(EquipeCad, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    

class EquipeUpdate(UpdateView):
    modal = Equipe
    template_name = 'cadastroEquipe.html'
    success_url = reverse_lazy('relatorio:equipes')
    form_class = EquipeForm
    
    def get_form_kwargs(self):
        
        kwargs = super(EquipeUpdate, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    
    def get_queryset(self):
        item = Equipe.objects.all()
        
        return item

    
class EquipeDelete(DeleteView):
    modal = Equipe
    template_name = 'cadastroEquipe.html'
    success_url = reverse_lazy('relatorio:equipes')
    def get_queryset(self):
        item = Equipe.objects.all()
        
        return item
    
class Impview(TemplateView):
    model = Relatorio
    template_name = "imprimir.html"    
    
@login_required(login_url='/signin/')
def pagina_principal (request):
    
    relatorios = Relatorio.objects.filter(usuario = request.user)
    relatorios_total = relatorios.count()
    equipes_total = Equipe.objects.all().count()
    
    context = {'relatorios': relatorios_total, 'equipes': equipes_total}
    return render(request,'pagina_principal.html', context)
   
    
    # Generate CSV File Venue List
def venue_csv(request):
        dados = request.GET.get('mes')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=venues.csv'
	
	# Create a csv writer
        writer = csv.writer(response)

	# Designate The Model
    
        venues = Relatorio.objects.filter(mes__icontains=dados)

	# Add column headings to the csv file
        writer.writerow(['Usuario', 'Codigo do Cliente', 'Frequencia', 'Data', 'Mes', 'Data Criacao'])     
	# Loop Thu and output
        for venue in venues:
              writer.writerow([venue.usuario, venue.codigo, venue.frequencia, venue.data, venue.mes, venue.data_criacao])

        return response




 