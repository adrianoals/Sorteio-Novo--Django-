from django.db import models

class Bloco(models.Model):

    BLOCO_CHOICES = [
        ('A', 'A',),
        ('B', 'B',),
    ]
    bloco = models.CharField(max_length=100, unique=True, choices=BLOCO_CHOICES)

    def __str__(self):
        return self.bloco

class Apartamento(models.Model):
    
    APARTAMENTO_CHOICES = [
        ('Apto 01', 'Apto 01'),
        ('Apto 02', 'Apto 02'),
        ('Apto 11', 'Apto 11'),
        ('Apto 12', 'Apto 12'),
        ('Apto 13', 'Apto 13'),
        ('Apto 14', 'Apto 14'),
        ('Apto 15', 'Apto 15'),    
        ('Apto 16', 'Apto 16'),    
        ('Apto 21', 'Apto 21'),
        ('Apto 22', 'Apto 22'),
        ('Apto 23', 'Apto 23'),
        ('Apto 24', 'Apto 24'),
        ('Apto 25', 'Apto 25'),    
        ('Apto 26', 'Apto 26'),    
        ('Apto 31', 'Apto 31'),
        ('Apto 32', 'Apto 32'),
        ('Apto 33', 'Apto 33'),
        ('Apto 34', 'Apto 34'),
        ('Apto 35', 'Apto 35'),    
        ('Apto 36', 'Apto 36'),    
        ('Apto 41', 'Apto 41'),
        ('Apto 42', 'Apto 42'),
        ('Apto 43', 'Apto 43'),
        ('Apto 44', 'Apto 44'),
        ('Apto 45', 'Apto 45'),    
        ('Apto 46', 'Apto 46'),    
    ]

    numero_apartamento = models.CharField(max_length=50, choices=APARTAMENTO_CHOICES)
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('numero_apartamento', 'bloco',)  # Garante a unicidade da combinação

    def __str__(self):
        return f"{self.numero_apartamento} - Bloco {self.bloco.bloco}"


class Vaga(models.Model):

    VAGA_CHOICES = [
        ('Vaga 01', 'Vaga 01'),
        ('Vaga 02', 'Vaga 02'),
        ('Vaga 03', 'Vaga 03'),
        ('Vaga 04', 'Vaga 04'),
        ('Vaga 05', 'Vaga 05'), 
        ('Vaga 06', 'Vaga 06'), 
        ('Vaga 07', 'Vaga 07'), 
        ('Vaga 08', 'Vaga 08'), 
        ('Vaga 09', 'Vaga 09'), 
        ('Vaga 10', 'Vaga 10'), 
        ('Vaga 11', 'Vaga 11'), 
        ('Vaga 12', 'Vaga 12'), 
        ('Vaga 13', 'Vaga 13'), 
        ('Vaga 14', 'Vaga 14'), 
        ('Vaga 15', 'Vaga 15'), 
        ('Vaga 16', 'Vaga 16'), 
        ('Vaga 17', 'Vaga 17'), 
        ('Vaga 18', 'Vaga 18'), 
        ('Vaga 19', 'Vaga 19'), 
        ('Vaga 20', 'Vaga 20'), 
        ('Vaga 21', 'Vaga 21'), 
        ('Vaga 22', 'Vaga 22'), 
        ('Vaga 23', 'Vaga 23'), 
        ('Vaga 24', 'Vaga 24'), 
        ('Vaga 25', 'Vaga 25'), 
        ('Vaga 26', 'Vaga 26'), 
        ('Vaga 27', 'Vaga 27'), 
        ('Vaga 28', 'Vaga 28'), 
        ('Vaga 29', 'Vaga 29'), 
        ('Vaga 30', 'Vaga 30'), 
        ('Vaga 31', 'Vaga 31'), 
        ('Vaga 32', 'Vaga 32'), 
        ('Vaga 33', 'Vaga 33'), 
        ('Vaga 34', 'Vaga 34'), 
        ('Vaga 35', 'Vaga 35'), 
        ('Vaga 36', 'Vaga 36'),
        ('Vaga 37', 'Vaga 37'),
        ('Vaga 38', 'Vaga 38'),
        ('Vaga 39', 'Vaga 39'),
        ('Vaga 40', 'Vaga 40'),
        ('Vaga 41', 'Vaga 41'),
        ('Vaga 42', 'Vaga 42'),
        ('Vaga 43', 'Vaga 43'),
        ('Vaga 44', 'Vaga 44'),
        ('Vaga 45', 'Vaga 45'),
        ('Vaga 46', 'Vaga 46'),
        ('Vaga 47', 'Vaga 47'),
        ('Vaga 48', 'Vaga 48'),
        ('Vaga 49', 'Vaga 49'),
        ('Vaga 50', 'Vaga 50'),	

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
