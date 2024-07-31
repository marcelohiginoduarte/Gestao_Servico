from django.db import models


class Servico(models.Model):
    Status_projeto = [ 
        ("Em Programacao", "Em programacao"),
        ("Programado", "Programado"),
        ("Em execucao", "Em execucao"),
        ("Executado", "Executado"),
        ("Executado Fora Prazo", "Executado Fora Prazo"),
        ("Nao Executado", "Nao Executado"),
        ("Interropida", "Interropida"),
        ("Medicao", "Medicao"),
        ("Entregue", "Entregue"),
        ("Pago", "Pago"),
]
    Mes_Programacao = [
        ("Jan", "Janeiro"),
        ("Fev", "Fevereiro"),
        ("Mar", "Março"),
        ("Abr", "Abril"),
        ("Mai", "Maio"),
        ("Jun", "Junho"),
        ("Julho", "Julho"),
        ("Ago", "Agosto"),
        ("Set", "Setembro"),
        ("Out", "Outubro"),
        ("Nov", "Novembro"),
        ("Dez", "Desembro"),

    ]

    Projeto = models.CharField(max_length=12, unique=True)
    Nota = models.CharField(max_length=10, unique=True)
    Status = models.CharField(max_length= 30, choices=Status_projeto)
    Descricao = models.CharField(max_length=50)
    Local = models.CharField(max_length=50)
    Data_Inicio = models.DateField(blank=True, null=True)
    Mes_servico = models.CharField(max_length=30, choices=Mes_Programacao,)
    ano_servico = models.CharField(max_length=4)
    Data_Fim = models.DateField(blank=True, null=True)
    Data_Programacao = models.DateField(blank=True, null=True)
    evidencia_execucao = models.ImageField(blank=True, null=True, upload_to="imagens/")
    Equipe = models.CharField(max_length=5, blank=True, null=True,)
    valor_inicial = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,)
    valor_final = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, )
    

    def __str__(self) -> str:
        return self.Projeto



class Equipe(models.Model):
    NumeroEquipe = models.CharField(max_length=5)
    Nome_Encaregado = models.CharField(max_length=100)
    Matricula_Encaregado = models.CharField(max_length=100)
    Nome_Eletricista_1 = models.CharField(max_length=100)
    Matricula_Eletricista1 = models.CharField(max_length=8)
    Nome_Eletricista_2 = models.CharField(max_length=100)
    Matricula_Eletricista2 = models.CharField(max_length=8)
    Nome_Eletricista_3 = models.CharField(max_length=100)
    Matricula_Eletricista3 = models.CharField(max_length=8)
    Nome_Eletricista_4 = models.CharField(max_length=100)
    Matricula_Eletricista4 = models.CharField(max_length=8)
    Nome_Ajudante_1 = models.CharField(max_length=100)
    Matricula_Ajudante1 = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.NumeroEquipe
    
