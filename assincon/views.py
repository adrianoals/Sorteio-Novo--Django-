from django.shortcuts import render

def assincon_home(request):
    	return render(request, 'assincon/assincon_home.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ListaSindicos
import random

def assincon_sorteio(request):
    sindicos_disponiveis = ListaSindicos.objects.all()
    sorteio_finalizado = False
    sindico_selecionado = None

    if request.method == 'POST' and sindicos_disponiveis:
        sindico_selecionado = random.choice(sindicos_disponiveis)
        sorteio_finalizado = True
        messages.success(request, f'O síndico selecionado é: {sindico_selecionado.nome}')
        return render(request, 'assincon/assincon_sorteio.html', {"sorteio_finalizado": sorteio_finalizado, "sindico_selecionado": sindico_selecionado})
    else:
        return render(request, 'assincon/assincon_sorteio.html', {"sorteio_finalizado": sorteio_finalizado, "sindicos_disponiveis": sindicos_disponiveis})
