from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Fornecedor(models.Model):
    UF_CHOICES = [
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    ]  # No UF_Choices, primeira parte é como salva, segunda parte é como aparece pro usuario
    nome = models.CharField(max_length=200, blank=False, null=False, verbose_name='Nome do Fornecedor')
    cnpj = models.CharField(
        max_length=14, blank=False, null=False, validators=[MinLengthValidator(14)]
    )
    endereco = models.CharField(max_length=500, blank=False, null=False, verbose_name ='Endereço')
    bairro = models.CharField(max_length=50, blank=False, null=False)
    cidade = models.CharField(max_length=50, blank=False, null=False)
    uf = models.CharField(
        max_length=2, choices=UF_CHOICES, verbose_name="UF", blank=False, null=False
    )
    telefone = models.CharField(
        max_length=15, blank=False, null=False, validators=[MinLengthValidator(11)]
    )
    email = models.EmailField(blank=False, null=False)
    transportadora_principal = models.CharField(max_length=300, blank=False, null=False, verbose_name='Transportadora Principal')
    outras_informacoes = models.CharField(max_length=500, blank=True, null=True, verbose_name='Outras Informações')
    outras_opcoes_de_contato = models.CharField(max_length=500, blank=True, null=True, verbose_name='Outras Opções de Contato')
    site = models.CharField(max_length=100, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):

    nome_do_produto = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nome do Produto')
    descricao = models.CharField(max_length=500, blank=False, null=False, verbose_name = 'Descrição')
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    custo_medio_de_compra = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Custo Médio de Compra'
    )
    data_cadastro = models.DateTimeField(auto_now_add=True)
    fornecedor = models.ForeignKey(
        Fornecedor, on_delete=models.CASCADE, related_name="produtos"
    )
