from django.db import models
from datetime import datetime
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    resumo = models.TextField()
    conteudo = CKEditor5Field(config_name='extends', )
    imagem_capa = models.ImageField(null = True, blank= True, upload_to='static/blog/')
    data_publicacao = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.autor} - {self.titulo}'