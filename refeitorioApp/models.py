from django.db import models
from PIL import Image

# Create your models here.
class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome_aluno = models.CharField(max_length=255, null=False)
    matricula_aluno = models.CharField(max_length=255, null=False)
    foto_aluno = models.ImageField(blank=True, null=True)

    def save(self):
        super().save()
        im = Image.open(self.foto_aluno.path)
        novo_tamanho = (100, 100)
        im.thumbnail(novo_tamanho)
        im.save(self.foto_aluno.path)

    def foto_url(self):
        if self.foto_aluno and hasattr(self.foto_aluno, 'url'):
            return self.foto_aluno.url
        else:
            return self.nome_aluno

    def __str__(self):
       return self.nome_aluno


class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nome_evento = models.CharField(max_length=255, null=False)
    foto_evento = models.ImageField(blank=True, null=True)
    id_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno')

    def save(self):
        super().save()
        im = Image.open(self.foto_evento.path)
        novo_tamanho = (100, 100)
        im.thumbnail(novo_tamanho)
        im.save(self.foto_evento.path)

    def foto_url(self):
        if self.foto_evento and hasattr(self.foto_evento, 'url'):
            return self.foto_evento.url
        else:
            return self.nome_evento

    def __str__(self):
       return self.nome_evento