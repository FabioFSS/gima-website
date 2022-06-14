from django.urls import path
from .views import ColaboradoresView, ContatoView, EventosView, IndexView, MinicursosView, ProjetosView, ProjetoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('colaboradores/', ColaboradoresView.as_view(), name='colaboradores'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('minicursos/', MinicursosView.as_view(), name='minicursos'),
    path('eventos/', EventosView.as_view(), name='eventos'),
    path('projetos/', ProjetosView.as_view(), name='projetos'),
    path('projeto/<int:pk>', ProjetoView.as_view(), name='projeto'),
]
