from calendar import c
from enum import auto
from django.views.generic import TemplateView
from .models import Arquivo, Minicurso, Ministrante, Participacao, Projeto, Video, Evento

class IndexView(TemplateView):
    template_name = 'index.html'

class ColaboradoresView(TemplateView):
    template_name = 'colaboradores.html'

class ContatoView(TemplateView):
    template_name = 'contato.html'

class MinicursosView(TemplateView):
    template_name = 'minicursos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minicursos'] = Minicurso.objects.all()

        return context

class MinicursoView(TemplateView):
    template_name = 'minicurso.html'

    def get_context_data(self, **kwargs):
        course_id = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['minicurso'] = Minicurso.objects.get(id=course_id)
        context['ministrantes'] = Ministrante.objects.filter(fk_minicurso=course_id)
        context['videos'] = Video.objects.filter(fk_minicurso=course_id)
        context['arquivos'] = Arquivo.objects.filter(fk_minicurso=course_id)

        return context

class EventosView(TemplateView):
    template_name = 'eventos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos'] = Evento.objects.all()

        return context

class EventoView(TemplateView):
    template_name = 'evento.html'

    def get_context_data(self, **kwargs):
        event_id = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['evento'] = Evento.objects.get(id=event_id)
        context['minicursos'] = Minicurso.objects.filter(fk_evento=event_id)

        return context

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


    