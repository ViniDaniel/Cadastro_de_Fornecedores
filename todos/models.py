from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    cnpj = models.CharField(max_length=14, blank=False, null=False, validators=[MinLengthValidator(14)])
    endereco = models.CharField(max_length=500, blank=False, null=False)
    bairro = models.CharField(max_length=50, blank=False, null=False)
    cidade = models.CharField(max_length=50, blank=False, null=False)
    uf = models.CharField(max_length=2, blank=False, null=False)
    telefone = models.CharField(max_length=15, blank=False, null=False, validators=[MinLengthValidator(11)])
    email = models.EmailField(blank=False, null=False)
    tipo_de_produto = models.CharField(max_length=200, blank=False, null=False)
    sobre_produto = models.CharField(max_length=500, blank=False, null=False)
    transportadora_principal = models.CharField(max_length=300, blank=False, null=False)
    custo_medio_de_compra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    outras_informações = models.CharField(max_length=500, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
