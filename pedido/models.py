from django.db import models
from django.contrib.auth.models import User


class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField(default=0)
    qtd_total = models.PositiveIntegerField()
    status = models.CharField(
        default="C",
        max_length=1,
        choices=(
            ('A', 'Aprovado'),
            ('A', 'Criado'),
            ('A', 'Reprovado'),
            ('A', 'Pendente'),
            ('A', 'Enviado'),
            ('A', 'Finalizado')
        ))

    def __str__(self):
        return f'Pedido N {self.pk}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.PositiveIntegerField(default=0)
    variacao = models.CharField(max_length=255)
    preco = models.FloatField()
    preco_promocional = models.FloatField()
    quantidade = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(
        upload_to='produto_imagens/%Y/%m/',
        blank=True, null=True)

    def __str__(self):
        return self.pedido

    class Meta:
        verbose_name = "Item Pedido"
        verbose_name_plural = "Itens Pedido"
