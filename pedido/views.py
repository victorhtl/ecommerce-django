from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


# host/pedido
class Pagar(View):
    pass


# host/pedido/fecharpedido
class FecharPedido(View):
    pass


# host/pedido/detalhe/<int:pk>
class Detalhe(View):
    pass
