from django.contrib import admin
from .models import Participacao, Projeto, Video, Arquivo, Autor, TipoArquivo, TipoAutor, TipoVideo


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
