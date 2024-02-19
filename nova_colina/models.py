from django.db import models

class Apartamento(models.Model):
    
    APARTAMENTO_CHOICES = [
        ('Apto 01', 'Apto 01'),
        ('Apto 02', 'Apto 02'),
        ('Apto 03', 'Apto 03'),
        ('Apto 04', 'Apto 04'),
        ('Apto 05', 'Apto 05'),
        ('Apto 06', 'Apto 06'),
        ('Apto 07', 'Apto 07'),
        ('Apto 08', 'Apto 08'),
        ('Apto 09', 'Apto 09'),
        ('Apto 10', 'Apto 10'),            
    ]

    numero_apartamento = models.CharField(max_length=50, choices=APARTAMENTO_CHOICES)

    def __str__(self):
        return f"{self.numero_apartamento}"


class VagaSimples(models.Model):

    VAGA_SIMPLES_CHOICES = [
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

    ]

    vaga_simples = models.CharField(max_length=50, unique=True, choices=VAGA_SIMPLES_CHOICES)

    def __str__(self):
        return self.vaga_simples

class VagaDupla(models.Model):

    VAGA_DUPLA_CHOICES = [
        ('Vaga 01 e 02', 'Vaga 01 e 02'),
        ('Vaga 03 e 04', 'Vaga 03 e 04'),
        ('Vaga 05 e 06', 'Vaga 05 e 06'),
        ('Vaga 07 e 08', 'Vaga 07 e 08'),
        ('Vaga 09 e 10', 'Vaga 09 e 10'),
        ('Vaga 11 e 12', 'Vaga 11 e 12'),
        ('Vaga 13 e 14', 'Vaga 13 e 14'),
        ('Vaga 15 e 16', 'Vaga 15 e 16'),
        ('Vaga 17 e 18', 'Vaga 17 e 18'),
        ('Vaga 19 e 20', 'Vaga 19 e 20'),
    ]

    vaga_dupla = models.CharField(max_length=50, unique=True, choices=VAGA_DUPLA_CHOICES)

    def __str__(self):
        return self.vaga_dupla


class Sorteio(models.Model):
    apartamento = models.OneToOneField(Apartamento, on_delete=models.CASCADE)
    vaga_simples = models.OneToOneField(VagaSimples, on_delete=models.CASCADE)
    vaga_dupla = models.OneToOneField(VagaDupla, on_delete=models.CASCADE)

    def __str__(self):
        # Acesso ao bloco através do apartamento
        return f"Apartamento {self.apartamento.numero_apartamento}  Vaga-simples {self.vaga_simples.vaga_simples} Vaga-Dupla {self.vaga_dupla.vaga_dupla}"


