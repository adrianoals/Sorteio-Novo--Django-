from django.contrib import admin
from assincon.models import ListaPresenca

class ListaPresencaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'brinde')
    list_display_links = ('id', 'nome', 'brinde')	

admin.site.register(ListaPresenca, ListaPresencaAdmin)

