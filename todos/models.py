from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Fornecedor(models.Model):
    UF_CHOICES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]
    nome = models.CharField(max_length=200, blank=False, null=False)
    cnpj = models.CharField(max_length=14, blank=False, null=False, validators=[MinLengthValidator(14)])
    endereco = models.CharField(max_length=500, blank=False, null=False)
    bairro = models.CharField(max_length=50, blank=False, null=False)
    cidade = models.CharField(max_length=50, blank=False, null=False)
    uf = models.CharField(max_length=2, choices=UF_CHOICES, verbose_name="UF",blank=False, null=False)
    telefone = models.CharField(max_length=15, blank=False, null=False, validators=[MinLengthValidator(11)])
    email = models.EmailField(blank=False, null=False)
    tipo_de_produto = models.CharField(max_length=200, blank=False, null=False)
    sobre_produto = models.CharField(max_length=500, blank=False, null=False)
    transportadora_principal = models.CharField(max_length=300, blank=False, null=False)
    custo_medio_de_compra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    outras_informações = models.CharField(max_length=500, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
