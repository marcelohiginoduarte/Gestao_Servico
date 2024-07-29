"""
URL configuration for Setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Meuprojeto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastroservico/', views.cadastrar_servico, name='cadastroservico'),
    path('cadastroequipe/', views.cadastro_equipes, name='cadastroequipe'),
    path('visualizar_servicos/', views.visualizar_servicos, name='visualizar_servicos'),
    path('visualizarequipe/', views.visualizar_equipes, name='visualiazarequipes'),
    path('visualizar_medicao', views.visualizar_medicao, name='visualizarmedicao'),
    path('atualizarservico/<int:pk>/', views.fazer_update.as_view(), name='fazer_update'),
    path('teste/', views.teste, name='teste'),
]
