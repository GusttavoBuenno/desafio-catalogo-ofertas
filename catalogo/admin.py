from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'percentual_desc', 'tipo_entrega', 'frete_gratis')
    search_fields = ('nome',)
