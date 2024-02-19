from django.db import models

class Apartamento(models.Model):
    
    APARTAMENTO_CHOICES = [
        ('Apto 0101', 'Apto 0101'),
        ('Apto 0102', 'Apto 0102'),
        ('Apto 0103', 'Apto 0103'),
        ('Apto 0104', 'Apto 0104'),        
        ('Apto 0201', 'Apto 0201'),
        ('Apto 0202', 'Apto 0202'),
        ('Apto 0203', 'Apto 0203'),
        ('Apto 0204', 'Apto 0204'),        
        ('Apto 0301', 'Apto 0301'),
        ('Apto 0302', 'Apto 0302'),
        ('Apto 0303', 'Apto 0303'),
        ('Apto 0304', 'Apto 0304'),        
        ('Apto 0401', 'Apto 0401'),
        ('Apto 0402', 'Apto 0402'),
        ('Apto 0403', 'Apto 0403'),
        ('Apto 0404', 'Apto 0404'),
        ('Apto 0501', 'Apto 0501'),
        ('Apto 0502', 'Apto 0502'),
        ('Apto 0503', 'Apto 0503'),
        ('Apto 0504', 'Apto 0504'),
        ('Apto 0601', 'Apto 0601'),
        ('Apto 0602', 'Apto 0602'),
        ('Apto 0603', 'Apto 0603'),
        ('Apto 0604', 'Apto 0604'),
        ('Apto 0701', 'Apto 0701'),
        ('Apto 0702', 'Apto 0702'),
        ('Apto 0703', 'Apto 0703'),
        ('Apto 0704', 'Apto 0704'),
        ('Apto 0801', 'Apto 0801'),
        ('Apto 0802', 'Apto 0802'),
        ('Apto 0803', 'Apto 0803'),
        ('Apto 0804', 'Apto 0804'),
        ('Apto 0901', 'Apto 0901'),
        ('Apto 0902', 'Apto 0902'),
        ('Apto 0903', 'Apto 0903'),
        ('Apto 0904', 'Apto 0904'),
        ('Apto 1001', 'Apto 1001'),
        ('Apto 1002', 'Apto 1002'),
        ('Apto 1003', 'Apto 1003'),
        ('Apto 1004', 'Apto 1004'),
        ('Apto 1101', 'Apto 1101'),
        ('Apto 1102', 'Apto 1102'),
        ('Apto 1103', 'Apto 1103'),
        ('Apto 1104', 'Apto 1104'),
        ('Apto 1201', 'Apto 1201'),
        ('Apto 1202', 'Apto 1202'),
        ('Apto 1203', 'Apto 1203'),
        ('Apto 1204', 'Apto 1204'),
        ('Apto 1301', 'Apto 1301'),
        ('Apto 1302', 'Apto 1302'),
        ('Apto 1303', 'Apto 1303'),
        ('Apto 1304', 'Apto 1304'),
        ('Apto 1401', 'Apto 1401'),
        ('Apto 1402', 'Apto 1402'),
        ('Apto 1403', 'Apto 1403'),
        ('Apto 1404', 'Apto 1404'),        
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
        ('Vaga 51', 'Vaga 51'),
        ('Vaga 52', 'Vaga 52'),
        ('Vaga 53', 'Vaga 53'),
        ('Vaga 54', 'Vaga 54'),
        ('Vaga 55', 'Vaga 55'),
        ('Vaga 56', 'Vaga 56'),
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
        ('Vaga 21 e 22', 'Vaga 21 e 22'),
        ('Vaga 23 e 24', 'Vaga 23 e 24'),
        ('Vaga 25 e 26', 'Vaga 25 e 26'),
        ('Vaga 27 e 28', 'Vaga 27 e 28'),
        ('Vaga 29 e 30', 'Vaga 29 e 30'),
        ('Vaga 31 e 32', 'Vaga 31 e 32'),
        ('Vaga 33 e 34', 'Vaga 33 e 34'),
        ('Vaga 35 e 36', 'Vaga 35 e 36'),
        ('Vaga 37 e 38', 'Vaga 37 e 38'),
        ('Vaga 39 e 40', 'Vaga 39 e 40'),
        ('Vaga 41 e 42', 'Vaga 41 e 42'),
        ('Vaga 43 e 44', 'Vaga 43 e 44'),
        ('Vaga 45 e 46', 'Vaga 45 e 46'),
        ('Vaga 47 e 48', 'Vaga 47 e 48'),
        ('Vaga 49 e 50', 'Vaga 49 e 50'),
        ('Vaga 51 e 52', 'Vaga 51 e 52'),
        ('Vaga 53 e 54', 'Vaga 53 e 54'),
        ('Vaga 55 e 56', 'Vaga 55 e 56'),
        ('Vaga 57 e 58', 'Vaga 57 e 58'),
        ('Vaga 59 e 60', 'Vaga 59 e 60'),
        ('Vaga 61 e 62', 'Vaga 61 e 62'),
        ('Vaga 63 e 64', 'Vaga 63 e 64'),
        ('Vaga 65 e 66', 'Vaga 65 e 66'),
        ('Vaga 67 e 68', 'Vaga 67 e 68'),
        ('Vaga 69 e 70', 'Vaga 69 e 70'),
        ('Vaga 71 e 72', 'Vaga 71 e 72'),
        ('Vaga 73 e 74', 'Vaga 73 e 74'),
        ('Vaga 75 e 76', 'Vaga 75 e 76'),
        ('Vaga 77 e 78', 'Vaga 77 e 78'),
        ('Vaga 79 e 80', 'Vaga 79 e 80'),
        ('Vaga 81 e 82', 'Vaga 81 e 82'),
        ('Vaga 83 e 84', 'Vaga 83 e 84'),
        ('Vaga 85 e 86', 'Vaga 85 e 86'),
        ('Vaga 87 e 88', 'Vaga 87 e 88'),
        ('Vaga 89 e 90', 'Vaga 89 e 90'),
        ('Vaga 91 e 92', 'Vaga 91 e 92'),
        ('Vaga 93 e 94', 'Vaga 93 e 94'),
        ('Vaga 95 e 96', 'Vaga 95 e 96'),
        ('Vaga 97 e 98', 'Vaga 97 e 98'),
        ('Vaga 99 e 100', 'Vaga 99 e 100'),
        ('Vaga 101 e 102', 'Vaga 101 e 102'),
        ('Vaga 103 e 104', 'Vaga 103 e 104'),
        ('Vaga 105 e 106', 'Vaga 105 e 106'),
        ('Vaga 107 e 108', 'Vaga 107 e 108'),
        ('Vaga 109 e 110', 'Vaga 109 e 110'),
        ('Vaga 111 e 112', 'Vaga 111 e 112'),
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


