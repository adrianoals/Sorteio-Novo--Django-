from django.db import models

class ListaDePresenca(models.Model):
    nome = models.CharField(max_length=150,)
    def __str__(self):
        return f'{self.nome}'
