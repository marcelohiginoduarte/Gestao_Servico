import django_filters
from Meuprojeto.models import Servico


class filtar_servico(django_filters.FilterSet):
    class Meta:
        model = Servico
        fields ={
            "Projeto":["icontains"],
            "Status":["icontains"],
        }

class filtar_medicao(django_filters.FilterSet):
    class Meta:
        model = Servico
        fields ={
            "Projeto":["icontains"],
        }