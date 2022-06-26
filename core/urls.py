from django.urls import path
from .views import ColaboradoresView, ContatoView, EventosView, IndexView, MinicursosView, ProjetosView, ProjetoView, EventoView, MinicursoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('colaboradores/', ColaboradoresView.as_view(), name='colaboradores'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('minicursos/', MinicursosView.as_view(), name='minicursos'),
    path('minicurso/<int:pk>', MinicursoView.as_view(), name='minicurso'),
    path('eventos/', EventosView.as_view(), name='eventos'),
    path('evento/<int:pk>', EventoView.as_view(), name='evento'),
    path('projetos/', ProjetosView.as_view(), name='projetos'),
    path('projeto/<int:pk>', ProjetoView.as_view(), name='projeto'),
]
