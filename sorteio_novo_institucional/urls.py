from django.urls import path
from sorteio_novo_institucional.views import home

urlpatterns = [
        path('home', home, name='index'), 
]