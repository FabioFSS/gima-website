from django.contrib import admin
from .models import Evento, Localizacao, Metodo, Minicurso, Ministrante, Participacao, Projeto, Video, Arquivo, Autor, TipoArquivo, TipoAutor, TipoVideo


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'objetivo', 'inicio', 'fim')


@admin.register(TipoVideo)
class TipoVideoAdmin(admin.ModelAdmin):
    list_display = ('tipo',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fk_tipo_video', 'link')


@admin.register(TipoArquivo)
class TipoArquivoAdmin(admin.ModelAdmin):
    list_display = ('tipo',)


@admin.register(Arquivo)
class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fk_tipo_arquivo', 'link')


@admin.register(TipoAutor)
class TipoAutorAdmin(admin.ModelAdmin):
    list_display = ('tipo',)


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fk_tipo_autor')


@admin.register(Participacao)
class ParticipacaoAdmin(admin.ModelAdmin):
    list_display = ('fk_projeto', 'fk_autor', 'orientador', 'bolsista')


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'resumo', 'inicio', 'fim', 'numero_dias')


@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('localizacao',)


@admin.register(Metodo)
class MetodoAdmin(admin.ModelAdmin):
    list_display = ('metodo',)

@admin.register(Minicurso)
class MinicursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'resumo', 'inicio', 'fim', 'numero_dias', 'fk_evento', 'fk_localizacao', 'fk_metodo')

@admin.register(Ministrante)
class MinistranteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fk_minicurso')