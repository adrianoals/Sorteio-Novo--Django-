from django.urls import path
from assincon.views import assincon_sorteio, assincon_lista

urlpatterns = [
        path('assincon', assincon_sorteio, name='assincon_sorteio'), 
        path('assincon_lista', assincon_lista, name='assincon_lista'), 
]