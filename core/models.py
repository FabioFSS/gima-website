from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.TextField()
    objetivos = models.TextField()
    periodo = models.CharField(max_length=100)

class Aula(models.Model):
    introducao = models.TextField()
    video = models.TextField()
    roteiro_pratica = models.TextField()
    projeto_fk = models.ForeignKey(Projeto, on_delete=models.CASCADE)