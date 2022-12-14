# Generated by Django 4.1.1 on 2022-10-01 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itempedido',
            options={'verbose_name': 'Item Pedido', 'verbose_name_plural': 'Itens Pedido'},
        ),
        migrations.AddField(
            model_name='pedido',
            name='qtd_total',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('A', 'Aprovado'), ('A', 'Criado'), ('A', 'Reprovado'), ('A', 'Pendente'), ('A', 'Enviado'), ('A', 'Finalizado')], default='C', max_length=1),
        ),
    ]
