from django.urls import path
from chacara_bom_sucesso.views import index, exportar_para_excel, zerar

urlpatterns = [
        path('chacara-bom-sucesso', index, name='index'), 
        path('exportar_para_excel/', exportar_para_excel, name='exportar_para_excel'),
        path('chacara-bom-sucesso-zerar/', zerar, name='zerar'),

]
