from django.urls import path
from nova_colina.views import nova_colina, zerar, excel_nova_colina

urlpatterns = [
        path('nova-colina', nova_colina, name='nova_colina'), 
        path('excel_nova_colina/', excel_nova_colina, name='excel_nova_colina'),
        path('nova-colina-zerar/', zerar, name='zerar'),

]
