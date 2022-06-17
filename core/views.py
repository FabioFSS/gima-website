from enum import auto
from django.views.generic import TemplateView
from .models import Arquivo, Participacao, Projeto, Autor, Video

class IndexView(TemplateView):
    template_name = 'index.html'

class ColaboradoresView(TemplateView):
    template_name = 'colaboradores.html'

class ContatoView(TemplateView):
    template_name = 'contato.html'

class MinicursosView(TemplateView):
    template_name = 'minicursos.html'

class EventosView(TemplateView):
    template_name = 'eventos.html'

class ProjetosView(TemplateView):
    template_name ='projetos.html'

    def get_context_data(self, **kwargs):
        context = super(ProjetosView, self).get_context_data(**kwargs)
        context['projetos'] = Projeto.objects.all() 

        return context

class ProjetoView(TemplateView):
    template_name = 'projeto.html'

    def get_context_data(self, **kwargs):
        project_id = self.kwargs.get('pk')
        context = super(ProjetoView, self).get_context_data(**kwargs)
        context['projeto'] = Projeto.objects.get(id=project_id)
        context['participacoes'] = Participacao.objects.filter(fk_projeto=project_id)
        context['videos'] = Video.objects.filter(fk_projeto=project_id)
        context['arquivos'] = Arquivo.objects.filter(fk_projeto=project_id)

        return context


    