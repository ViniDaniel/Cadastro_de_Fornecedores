# Generated by Django 5.0.6 on 2024-10-28 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0005_remove_fornecedor_custo_medio_de_compra_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="fornecedor",
            name="outras_opcoes_de_contato",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]