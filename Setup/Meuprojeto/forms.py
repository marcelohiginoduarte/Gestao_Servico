from django import forms
from Meuprojeto.models import Servico, Equipe

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['Projeto', 'Nota', 'Status', 'Descricao', 'Local', 'Data_Inicio', 'Data_Fim', 'Data_Programacao', 'Equipe', 'valor_inicial', 'valor_final']

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['NumeroEquipe', 'Nome_Encaregado', 'Matricula_Encaregado', 'Nome_Eletricista_1', 'Matricula_Eletricista1', 'Nome_Eletricista_2', 'Matricula_Eletricista2', 'Nome_Eletricista_3', 'Matricula_Eletricista3', 'Nome_Eletricista_4', 'Matricula_Eletricista4', 'Nome_Ajudante_1', 'Matricula_Ajudante1']