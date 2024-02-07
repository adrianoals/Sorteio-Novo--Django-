from django.shortcuts import render

# Create your views here.
def home(request):
    	return render(request, 'sorteio_novo_institucional/home.html')

def solucoes(request):
    	return render(request, 'sorteio_novo_institucional/solucoes.html')

def orcamento(request):
    	return render(request, 'sorteio_novo_institucional/orcamento.html')

def contato(request):
    	return render(request, 'sorteio_novo_institucional/contato.html')
