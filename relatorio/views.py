from http.client import NOT_FOUND
from django.http import Http404
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from accounts.models.user import Gestor, User
from relatorio.forms import EquipeForm
from .models import Equipe, Relatorio
from django.http import HttpResponse
from django.contrib.auth import get_user
from django.template import RequestContext

import csv



class RelatorioCad(CreateView, LoginRequiredMixin):
    login_url = '/signup/'
    model = Relatorio
    fields = [ "codigo_cliente","frequencia", "data","mes"]
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
    context = {'info': relatoriox, 'eq': equipe, 'm':me, "usuario":user}
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
    
    def form_valid(self, form):
        gest = Gestor.objects.get(user_id = self.request.user.id)
        form.instance.gestor = gest
        
        url=  super().form_valid(form)
        
        return url
    

def equipeLista(request):
    gest = Gestor.objects.get(user_id = request.user.id)
    equipes = Equipe.objects.filter(gestor_id=gest)
  
    context = {'equipes': equipes }
    
    return render(request,'equipeLista.html', context )


   
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
        gest = Gestor.objects.get(user_id = self.request.user.id)
        item = Equipe.objects.filter(gestor_id = gest)
               
        return item
    

def handler404(request, exception):
    return render(request, '404.html')

class EquipeDelete(DeleteView):
    modal = Equipe
    template_name = 'cadastroEquipe.html'
    success_url = reverse_lazy('relatorio:equipes')
    def get_queryset(self):
        gest = Gestor.objects.get(user_id = self.request.user.id)
        item = Equipe.objects.filter(gestor = gest)
        
        return item
    
def listaFuncionario(request):
    equipes = Equipe.objects.filter(gestor_id=request.user.id)
    ok = User.objects.filter(equipe__in=equipes).distinct()

    context = {'func':ok}
    return render(request, 'listaFunc.html', context)
    
    
class Impview(TemplateView):
    model = Relatorio
    template_name = "imprimir.html"    
    
@login_required(login_url='/signin/')
def pagina_principal (request):
    
    relatorios = Relatorio.objects.filter(usuario = request.user)
    relatorios_total = relatorios.count()
    equipes_total = Equipe.objects.all().count()
    nome = User.objects.get(pk = request.user.id)
    
    context = {'relatorios': relatorios_total, 'equipes': equipes_total, "nome":nome}
    return render(request,'pagina_principal.html', context)
   
    
    # Generate CSV File Venue List
def venue_csv(request):
        dados = request.GET.get('mes')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=venues.csv'
	
	# Create a csv writer
        writer = csv.writer(response)

	# Designate The Model
    
        venues = Relatorio.objects.filter(mes__icontains=dados,usuario = request.user)

	# Add column headings to the csv file
        writer.writerow(['Codigo do vendedor','Vendedor', 'Codigo do Cliente', 'Frequencia', 'Data', 'Mes', 'Data Criacao'])     
	# Loop Thu and output
        for venue in venues:
              writer.writerow([venue.usuario.codigo,venue.usuario.nome, venue.codigo_cliente, venue.frequencia, venue.data, venue.mes, venue.data_criacao])

        return response




 