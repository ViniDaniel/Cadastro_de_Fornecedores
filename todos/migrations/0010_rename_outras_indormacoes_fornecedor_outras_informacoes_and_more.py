# Generated by Django 5.0.6 on 2024-11-03 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0009_alter_fornecedor_transportadora_principal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fornecedor',
            old_name='outras_indormacoes',
            new_name='outras_informacoes',
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='endereco',
            field=models.CharField(max_length=500, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='transportadora_principal',
            field=models.CharField(max_length=300, verbose_name='Transportadora Principal'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='custo_medio_de_compra',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Custo Médio de Compra'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.CharField(max_length=500, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome_do_produto',
            field=models.CharField(max_length=100, verbose_name='Nome do Produto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Preço'),
        ),
    ]
