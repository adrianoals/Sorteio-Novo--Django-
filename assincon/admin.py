from django.contrib import admin
from assincon.models import ListaPresenca, ListaSindicos

class ListaPresencaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'brinde')
    list_display_links = ('id', 'nome', 'brinde')	


class ListaSindicosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')	

admin.site.register(ListaPresenca, ListaPresencaAdmin)
admin.site.register(ListaSindicos, ListaSindicosAdmin)

