from django.shortcuts import render, redirect, get_object_or_404
from Meuprojeto.models import Servico, Equipe
from Meuprojeto.forms import ServicoForm, EquipeForm

def home(request):
    return render(request, 'home.html')

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
    
    return render(request, 'cadastrar_servico.html', {'form': form, 'erro': erro, 'texto': texto})


def cadastro_equipes(request):
    if request.method == "POST":
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visualizar_equipes')
    else:
        form = EquipeForm()
    return render(request, 'cadastro_equipes.html', {'form': form})

def visualizar_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'visualizar.html', {'visualizar_servicos': servicos})

def status_servico(request):
    status = request.GET.get('status', '')
    if not status:
        return 'Em Programacao'
    # Adicione lógica adicional para manipular diferentes status, se necessário
    return status



