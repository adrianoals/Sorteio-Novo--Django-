from django.urls import path
from assincon.views import assincon_home, assincon_sorteio

urlpatterns = [
        path('assincon-home', assincon_home, name='assincon_home'), 
        path('assincon-sorteio', assincon_sorteio, name='assincon_sorteio'), 
]