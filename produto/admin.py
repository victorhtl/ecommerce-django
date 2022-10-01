from django.contrib import admin
from .models import Produto, Variacao


class VariacaoInline(admin.TabularInline):
    model = Variacao


class ProdutoAdmin(admin.ModelAdmin):
    inlines = [VariacaoInline]


admin.site.register(Produto, ProdutoAdmin)
