from django.shortcuts import render, redirect
from Meuprojeto.models import Servico, Equipe

def home(request):
    return render(request, 'Home.html',)

def CadastrarServico(request):
    if request.method == "GET":
        erro = request.GET.get('erro')
        texto = request.GET.get('texto')
        return render (request, 'Cadastrarservico.html', {'erro': erro, 'texto':texto})
    if request.method == "POST":
        Projeto = request.POST.get('Projeto')
        Nota = request.POST.get('nota')
        Status = request.POST.get('status')
        Descricao = request.POST.get('Descricao')
        Local = request.POST.get('Local')
        Data_Inicio = request.POST.get('Data_Inicio')
        Data_Fim = request.POST.get('Data_Fim')
        Data_Programacao = request.POST.get('Data_Programacao')
        Equipe = request.POST.get('Equipe')
        valor_inicial = request.POST.get('valor_inicial')
        valor_final = request.POST.get('valor_final')

        if len(Projeto) <=7:
            return redirect('/cadastroservico/?erro=1&texto=Digite um projeto valido')
        

        servico = Servico(
            Projeto = Projeto,
            Nota = Nota,
            Status = Status,
            Descricao = Descricao,
            Local = Local,
            Data_Inicio = Data_Inicio,
            Data_Fim = Data_Fim,
            Data_Programacao = Data_Programacao,
            Equipe = Equipe,
            valor_inicial = valor_inicial,
            valor_final = valor_final
        )
        #Salvar os dados no banco de dados
        servico.save()
    return render(request, 'Cadastrarservico.html',)

def CadastroEquipes(request):
    if request.method == "GET":
        return render(request, 'Cadastroequipes.html')
    elif request.method == "POST":
        NumeroEquipe = request.POST.get('NumeroEquipe')
        Nome_Encaregado = request.POST.get('Nome_Encaregado')
        Matricula_Encaregado = request.POST.get('Matricula_Encaregado')
        Nome_Eletricista_1 = request.POST.get('Nome_Eletricista_1')
        Matricula_Eletricista1 = request.POST.get('Matricula_Eletricista1')
        Nome_Eletricista_2 = request.POST.get('Nome_Eletricista_2')
        Matricula_Eletricista2 = request.POST.get('Matricula_Eletricista2')
        Nome_Eletricista_3 = request.POST.get('Nome_Eletricista_3')
        Matricula_Eletricista3 = request.POST.get('Matricula_Eletricista3')
        Nome_Eletricista_4 = request.POST.get('Nome_Eletricista_4')
        Matricula_Eletricista4 = request.POST.get('Matricula_Eletricista4')
        Nome_Ajudante_1 = request.POST.get('Nome_Ajudante_1')
        Matricula_Ajudante1 = request.POST.get('Matricula_Ajudante1')


        equipe = Equipe(
           NumeroEquipe = NumeroEquipe,
           Nome_Encaregado = Nome_Encaregado,
           Matricula_Encaregado = Matricula_Encaregado,
           Nome_Eletricista_1 = Nome_Eletricista_1,
           Matricula_Eletricista1 = Matricula_Eletricista1,
           Nome_Eletricista_2 = Nome_Eletricista_2,
           Matricula_Eletricista2 = Matricula_Eletricista2,
           Nome_Eletricista_3 = Nome_Eletricista_3,
           Matricula_Eletricista3 = Matricula_Eletricista3,
           Nome_Eletricista_4 = Nome_Eletricista_4, 
           Matricula_Eletricista4 = Matricula_Eletricista4,
           Nome_Ajudante_1 = Nome_Ajudante_1,
           Matricula_Ajudante1 = Matricula_Ajudante1
        )

        equipe.save()
        return render(request, 'Cadastroequipes.html')
    

def VisualizarServicos(request):
    visualizar_servicos = Servico.objects.all()
    print(visualizar_servicos)
    return render(request, 'Visualizar.html', {'visualizer_servicos': visualizar_servicos})

def StatusServico(request):
    if Status == '':
        return 'Em Programacao'

