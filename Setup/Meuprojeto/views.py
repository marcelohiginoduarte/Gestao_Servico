from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from Meuprojeto.models import Servico, Equipe
from Meuprojeto.forms import ServicoForm, EquipeForm
from Meuprojeto.filters import filtar_servico
from django.urls import reverse_lazy
from django.views import View

def home(request):
    return render(request, 'Home.html')

def cadastrar_servico(request):
    erro = None
    texto = None
    
    if request.method == "POST":
        form = ServicoForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print(form.errors)
            form.save()
            return redirect('visualizar_servicos')
    else:
        form = ServicoForm()
        erro = request.GET.get('erro')
        texto = request.GET.get('texto')
    
    return render(request, 'teste.html', {'form': form, 'erro': erro, 'texto': texto})


def cadastro_equipes(request):
    if request.method == "POST":
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visualizarequipes')
    else:
        form = EquipeForm()
    return render(request, 'cadastro_equipes.html', {'form': form})


#essa linha, é a linha que visualiza todos os serviços.
def visualizar_servicos(request):
    servicos = Servico.objects.all()
    filtro = filtar_servico(request.GET, servicos)
    return render(request, 'visualizar_servicos.html', {'visualizar_servicos': filtro.qs, 'filter':filtro})


def visualizar_equipes(request):
    equipes = Equipe.objects.all()
    return render(request, 'visualizar_equipes.html', {'equipes':equipes})


def status_servico(request):
    status = request.GET.get('status', '')
    if not status:
        return 'Em Programacao'
    # Adicione lógica adicional para manipular diferentes status, se necessário
    return status


class fazer_update(UpdateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'editar_servico.html'
    fields = ['Projeto', 'Nota', 'Status', 'Descricao', 'Local', 'Data_Inicio', 'Data_Fim', 'Data_Programacao', 'Equipe', 'valor_inicial', 'valor_final']
    success_url = reverse_lazy('visualizar_servicos')


def teste(request):
    teste = Servico.objects.all()
    filtro_teste = filtar_servico(request.GET, teste)
    return render(request, 'cadastrar_servico.html', {'teste': filtro_teste.qs, 'filter': filtro_teste})

def visualizar_medicao(request):
    medicao = Servico.objects.filter(Status='Medicao')
    return render(request, 'visualizar_medicao.html', {'medicao':medicao})

class servico_lista(ListView):
    model = Servico
    queryset = Servico.objects.all()
    template_name = 'cadastrar_servico.html'

def filtrtrarunitario(request):
    tudo = Servico.objects.all()
    unitario=filtar_servico(request.GET, tudo)
    form.save()
    return render(request, 'cadastrar_servico.html', {'tudo':unitario.qs, 'filter':unitario})

