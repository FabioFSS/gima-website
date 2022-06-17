from django.db import models


class Projeto(models.Model):
    titulo = models.CharField('Título', max_length=200)
    objetivo = models.TextField('Objetivo')
    inicio = models.DateField('Início')
    fim = models.DateField('Fim')

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.titulo


class TipoVideo(models.Model):
    TIPO_CHOICES = (
        ('apresentacao', 'Apresentação'),
        ('aula', 'Aula'),
    )

    tipo = models.CharField(
        'Tipo de vídeo', max_length=50, choices=TIPO_CHOICES)

    class Meta:
        verbose_name = 'Tipo de vídeo'
        verbose_name_plural = 'Tipos de vídeo'

    def __str__(self):
        return self.tipo


class Video(models.Model):
    titulo = models.CharField('Título do vídeo', max_length=200)
    link = models.CharField('Link do vídeo', max_length=200)
    fk_tipo_video = models.ForeignKey(
        'core.TipoVideo', on_delete=models.CASCADE)
    fk_projeto = models.ForeignKey('core.Projeto', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Vídeo'
        verbose_name_plural = 'Vídeos'

    def __str__(self):
        return self.titulo


class TipoArquivo(models.Model):
    TIPO_CHOICES = (
        ('resumo', 'Resumo'),
        ('roteiro', 'Roteiro'),
    )

    tipo = models.CharField(
        'Tipo de arquivo', max_length=50, choices=TIPO_CHOICES)

    class Meta:
        verbose_name = 'Tipo de arquivo'
        verbose_name_plural = 'Tipos de arquivo'

    def __str__(self):
        return self.tipo


class Arquivo(models.Model):
    titulo = models.CharField('Título do arquivo', max_length=200)
    link = models.CharField('Link do arquivo', max_length=200)
    fk_tipo_arquivo = models.ForeignKey(
        'core.TipoArquivo', on_delete=models.CASCADE)
    fk_projeto = models.ForeignKey('core.Projeto', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'

    def __str__(self):
        return self.titulo


class TipoAutor(models.Model):
    TIPO_CHOICES = (
        ('discente', 'Discente'),
        ('docente', 'Docente'),
    )

    tipo = models.CharField(
        'Tipo de video', max_length=50, choices=TIPO_CHOICES)

    class Meta:
        verbose_name = 'Tipo de video'
        verbose_name_plural = 'Tipos de video'

    def __str__(self):
        return self.tipo


class Autor(models.Model):
    nome = models.CharField('Nome do autor', max_length=200)
    fk_tipo_autor = models.ForeignKey(
        'core.TipoAutor', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nome


class Participacao(models.Model):
    orientador = models.BooleanField('Orientador')
    bolsista = models.BooleanField('Bolsista')
    fk_projeto = models.ForeignKey('core.Projeto', on_delete=models.CASCADE)
    fk_autor = models.ForeignKey('core.Autor', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Participação'
        verbose_name_plural = 'Participações'

    def __str__(self):
        return f'{self.fk_autor} participante de {self.fk_projeto}'
