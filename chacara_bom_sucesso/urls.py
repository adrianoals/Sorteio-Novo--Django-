from django.urls import path
from chacara_bom_sucesso.views import cbs_index, cbs_exportar_para_excel, cbs_zerar

urlpatterns = [
        path('chacara-bom-sucesso', cbs_index, name='cbs_index'), 
        path('exportar_para_excel/', cbs_exportar_para_excel, name='cbs_exportar_para_excel'),
        path('chacara-bom-sucesso-zerar/', cbs_zerar, name='cbs_zerar'),

]
