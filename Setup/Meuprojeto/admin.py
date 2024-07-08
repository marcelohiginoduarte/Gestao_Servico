from django.contrib import admin
from Meuprojeto.models import Servico, Equipe




class ListandoServico(admin.ModelAdmin):
    list_display = ("Projeto", "Nota", "Status")
    list_display_links = ("Projeto", "Nota")
    

class ListandoEquipe(admin.ModelAdmin):
    list_display = ("NumeroEquipe", "Nome_Encaregado", "Matricula_Encaregado")
    list_display_links = ("NumeroEquipe", "Nome_Encaregado", "Matricula_Encaregado")

admin.site.register(Servico,ListandoServico)
admin.site.register(Equipe, ListandoEquipe)
