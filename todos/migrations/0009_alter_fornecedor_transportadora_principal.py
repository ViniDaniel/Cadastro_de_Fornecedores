# Generated by Django 5.0.6 on 2024-10-31 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0008_remove_fornecedor_outras_informações_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='transportadora_principal',
            field=models.CharField(max_length=300, verbose_name='Transportatoda Principal'),
        ),
    ]
