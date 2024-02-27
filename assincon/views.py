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


# from django.shortcuts import render, redirect
# from .models import ListaSindicos, Sorteio
# import random

# def assincon_sorteio(request):
#     for sindico in ListaSindicos.objects.all():
#         Sorteio.objects.get_or_create(sindico=sindico)

#     sindicos_nao_sorteados = Sorteio.objects.filter(sorteado=False)
#     sorteio_finalizado = not sindicos_nao_sorteados.exists()

#     sindico_selecionado = None

#     if request.method == 'POST' and not sorteio_finalizado:
#         sindico_selecionado = random.choice(sindicos_nao_sorteados)
#         sindico_selecionado.sorteado = True
#         sindico_selecionado.save()
#         request.session['sindico_selecionado_id'] = sindico_selecionado.id  # Salva o id do sindico sorteado na sessão
#         return redirect('/assincon-sorteio')  # Use o nome da url da view para redirecionar

#     if 'sindico_selecionado_id' in request.session:
#         # Recupera o objeto sindico_selecionado usando o id armazenado na sessão
#         sindico_selecionado_id = request.session.get('sindico_selecionado_id')
#         sindico_selecionado = Sorteio.objects.get(id=sindico_selecionado_id)

#     context = {
#         'sorteio_finalizado': sorteio_finalizado,
#         'sindico_selecionado': sindico_selecionado,  # Passa o objeto para o template
#     }

#     return render(request, 'assincon/assincon_sorteio.html', context)


# def assincon_sorteio(request):
#     for sindico in ListaSindicos.objects.all():
#         Sorteio.objects.get_or_create(sindico=sindico)

#     sindicos_nao_sorteados = Sorteio.objects.filter(sorteado=False)
#     sorteio_finalizado = not sindicos_nao_sorteados.exists()

#     sindico_selecionado_msg = None  # Mensagem sobre o síndico sorteado

#     if request.method == 'POST' and not sorteio_finalizado:
#         sindico_selecionado = random.choice(sindicos_nao_sorteados)
#         sindico_selecionado.sorteado = True
#         sindico_selecionado.save()
#         sindico_selecionado_msg = f"Síndico sorteado é: {sindico_selecionado.sindico.nome}"
#         # Redirecionar pode limpar a mensagem, considere armazenar em sessão se necessário
#     else:
#         if sorteio_finalizado:
#             sindico_selecionado_msg = "Sorteio finalizado!"

#     context = {
#         'sorteio_finalizado': sorteio_finalizado,
#         'sindico_selecionado_msg': sindico_selecionado_msg,
#         # Inclua outros contextos necessários
#     }

#     return render(request, 'assincon/assincon_sorteio.html', context)
