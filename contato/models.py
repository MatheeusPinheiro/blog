from django.db import models

# Create your models here.

CHOICES_ASSSUNTO = (
    ('', 'Selecione um assunto'),
    ('descontos', 'Descontos'),
    ('consultoria', 'Consultoria'),
    ('freelance', 'Freelance'),
    ('elogios', 'Elogios'),
    ('reclamações', 'Reclamações'),
    ('outros', 'Outros'),
)

class Contato(models.Model):
    assunto = models.CharField(max_length=100, default="", choices= CHOICES_ASSSUNTO)
    nome = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100)
    mensagem = models.TextField(max_length=1000)


    def __str__(self):
        return f'{self.nome} - {self.email}'