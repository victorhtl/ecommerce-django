from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


# dominio/
# Mostra todos os produtos
class ListaProdutos(ListView):
    pass


# dominio/slug
class DetalhesProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse('slug')


# dominio/addtocart
class AddToCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Add')


# dominio/removefromcart
class RemoveFromCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('RemoveFC')


# dominio/finalizar
class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
