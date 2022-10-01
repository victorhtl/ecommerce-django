from django.urls import path
from . import views

app_name = 'produto'  # produto:lista

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista'),
    path('<slug>', views.DetalhesProdutos.as_view(), name='slug'),
    path('addtocart/', views.AddToCart.as_view(), name='addtocart'),
    path(
        'removefromcart/',
        views.RemoveFromCart.as_view(),
        name='removefromcart'),
    path('finalizar/', views.Finalizar.as_view(), name='finalizar')
]
