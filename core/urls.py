from django.urls import path
from .views import index, colaboradores, contato, minicursos, eventos, projetos

urlpatterns = [
    path('', index, name='index'),
    path('colaboradores/', colaboradores, name='colaboradores'),
    path('contato/', contato, name='contato'),
    path('minicursos/', minicursos, name='minicursos'),
    path('eventos/', eventos, name='eventos'),
    path('projetos/', projetos, name='projetos'),
]
