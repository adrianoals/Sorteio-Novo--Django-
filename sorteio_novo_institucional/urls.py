from django.urls import path
from sorteio_novo_institucional.views import home, solucoes, orcamento, contato

urlpatterns = [
        path('', home, name='home'), 
        path('solucoes', solucoes, name='solucoes'), 
        path('orcamento', orcamento, name='orcamento'), 
        path('contato', contato, name='contato'), 
]


