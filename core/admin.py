from django.contrib import admin
from .models import Projeto, Aula

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autores')


class AulaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero', 'projeto_fk')


admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Aula, AulaAdmin)