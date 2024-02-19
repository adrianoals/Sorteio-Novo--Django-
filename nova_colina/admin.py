from django.contrib import admin
from nova_colina.models import Apartamento, VagaSimples, VagaDupla, Sorteio


class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_apartamento')
    list_display_links = ('id', 'numero_apartamento')

class VagaSimplesAdmin(admin.ModelAdmin):
    list_display = ('id', 'vaga_simples')
    list_display_links = ('id', 'vaga_simples')

class VagaDuplaAdmin(admin.ModelAdmin):
    list_display = ('id', 'vaga_dupla')
    list_display_links = ('id', 'vaga_dupla')

class SorteioAdmin(admin.ModelAdmin):
    list_display = ('id', 'apartamento', 'vaga_simples', 'vaga_dupla')
    list_display_links = ('id', 'apartamento', 'vaga_simples', 'vaga_dupla')


admin.site.register(Apartamento, ApartamentoAdmin)
admin.site.register(VagaSimples, VagaSimplesAdmin)
admin.site.register(VagaDupla, VagaDuplaAdmin)
admin.site.register(Sorteio, SorteioAdmin)