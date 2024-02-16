from django.urls import path
from chacara_bom_sucesso.views import chacara_bom_sucesso, index, exportar_para_excel

urlpatterns = [
        path('chacara-bom-sucesso', chacara_bom_sucesso, name='chacara_bom_sucesso'), 
        path('chacara-bom-sucesso-index', index, name='index'), 
        path('exportar_para_excel/', exportar_para_excel, name='exportar_para_excel'),

]
