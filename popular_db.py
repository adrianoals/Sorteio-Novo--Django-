# Importar os modelos
from nova_colina.models import Apartamento, VagaSimples, VagaDupla

# Função para popular Apartamentos
def popular_apartamentos():
    for numero in Apartamento.APARTAMENTO_CHOICES:
        Apartamento.objects.get_or_create(numero_apartamento=numero[0])

# Função para popular Vagas Simples
def popular_vagas_simples():
    for vaga in VagaSimples.VAGA_SIMPLES_CHOICES:
        VagaSimples.objects.get_or_create(vaga_simples=vaga[0])

# Função para popular Vagas Duplas
def popular_vagas_duplas():
    for vaga in VagaDupla.VAGA_DUPLA_CHOICES:
        VagaDupla.objects.get_or_create(vaga_dupla=vaga[0])

# Executar as funções
if __name__ == "__main__":
    popular_apartamentos()
    popular_vagas_simples()
    popular_vagas_duplas()
