from django.db import models

class ListaPresenca(models.Model):
    nome = models.CharField(max_length=150,)
    brinde = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.nome}'

class ListaSindicos(models.Model):
    nome = models.CharField(max_length=150,)
    def __str__(self):
        return f'{self.nome}'

