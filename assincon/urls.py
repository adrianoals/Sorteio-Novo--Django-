from django.urls import path
from assincon.views import assincon_home

urlpatterns = [
        path('assincon-home', assincon_home, name='assincon_home'), 
]