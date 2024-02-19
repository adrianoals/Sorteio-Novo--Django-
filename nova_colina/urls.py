from django.urls import path
from nova_colina.views import nova_colina

urlpatterns = [
        path('nova-colina', nova_colina, name='nova_colina'), 
        # path('exportar_para_excel/', exportar_para_excel, name='exportar_para_excel'),

]
