import django_filters
from .models import Servico



class filtro_medicao(django_filters.filterset):
    class Meta:
        model = Servico
        fields = {
            'Status': ['Medicao']
        }