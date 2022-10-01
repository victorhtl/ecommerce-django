from django.contrib import admin
from .models import Pedido, ItemPedido


class InlineItemPedido(admin.TabularInline):
    model = ItemPedido


class PedidoAdmin(admin.ModelAdmin):
    inlines = [InlineItemPedido]


admin.site.register(Pedido, PedidoAdmin)
