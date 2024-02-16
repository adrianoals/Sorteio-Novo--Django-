from django.db import models

class Bloco(models.Model):

    BLOCO_CHOICES = [
        ('-', '-',)
    ]
    bloco = models.CharField(max_length=100, unique=True, choices=BLOCO_CHOICES, default='-')

    def __str__(self):
        return self.bloco

class Apartamento(models.Model):
    
    APARTAMENTO_CHOICES = [
        ('Apto 01', 'Apto 01'),
        ('Apto 02', 'Apto 02'),
        ('Apto 03', 'Apto 03'),
        ('Apto 04', 'Apto 04'),
        ('Apto 05', 'Apto 05'),    
    ]

    numero_apartamento = models.CharField(max_length=50, unique=True, choices=APARTAMENTO_CHOICES)
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.numero_apartamento} - Bloco {self.bloco.bloco}"

class Vaga(models.Model):

    VAGA_CHOICES = [
        ('Vaga 01', 'Vaga 01'),
        ('Vaga 02', 'Vaga 02'),
        ('Vaga 03', 'Vaga 03'),
        ('Vaga 04', 'Vaga 04'),
        ('Vaga 05', 'Vaga 05'), 
    ]

    vaga = models.CharField(max_length=50, unique=True, choices=VAGA_CHOICES)

    def __str__(self):
        return self.vaga


class Sorteio(models.Model):
    apartamento = models.OneToOneField(Apartamento, on_delete=models.CASCADE)
    vaga = models.OneToOneField(Vaga, on_delete=models.CASCADE)

    def __str__(self):
        # Acesso ao bloco através do apartamento
        return f"Apartamento {self.apartamento.numero_apartamento} - Bloco {self.apartamento.bloco.bloco} - Vaga {self.vaga.vaga}"
