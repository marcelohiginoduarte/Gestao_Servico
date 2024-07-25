from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from Meuprojeto.models import Servico, Equipe
from Meuprojeto.forms import ServicoForm, EquipeForm
from Meuprojeto.filters import filtar_servico
from django.urls import reverse_lazy

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
            return redirect('visualizar_equipes')
    else:
        form = EquipeForm()
    return render(request, 'cadastro_equipes.html', {'form': form})
#essa linha, é a linha que visualiza todos os serviços.
def visualizar_servicos(request):
    servicos = Servico.objects.all()
    filtro = filtar_servico(request.GET, servicos)
    return render(request, 'visualizar_servicos.html', {'visualizar_servicos': filtro.qs, 'filter':filtro})


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