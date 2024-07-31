import django_filters
from Meuprojeto.models import Servico


class filtar_servico(django_filters.FilterSet):
    class Meta:
        model = Servico
        fields ={
            "Projeto":["icontains"],
            "Status":["icontains"],
            "Mes_servico":["icontains"],
            "ano_servico":["icontains"],
        }

class filtar_medicao(django_filters.FilterSet):
    class Meta:
        model = Servico
        fields ={
            "Projeto":["icontains"],
        }