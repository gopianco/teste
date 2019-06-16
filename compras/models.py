from django.db import models
from django.utils import timezone

metodo_envio = (
    ('0414', 'SEDEX'),
    ('04510', 'PAC'),
    ('0215', 'SEDEX10'),
)


class Compra(models.Model):
    """
    Esta classe cria os modelos para uma compra e calcula o total da compra.
    Tem uma chave estrangeira na classe produto, atributo muitos p/ muitos onde acesso todos os produtos de uma compra.

    """
    __author__ = 'Giovane Pianco'
    __version__ = '0.2'
    __email__ = 'gopianco@hotmail.com'
    __status__ = 'Development'
    __maintainer__ = 'Giovane Pianco'

    id_compra = models.AutoField(primary_key=True)
    fornecedor = models.CharField(max_length=200, blank=True, null=True)
    produtos = models.ManyToManyField('produto')
    total_produtos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    qtd_produtos = models.IntegerField(default=1)
    valor_frete = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    metodo_envio = models.CharField(max_length=6, choices=metodo_envio, blank=True, null=True)
    tempo_envio = models.CharField(max_length=2, blank=True, null=True)
    codigo_rastreio = models.CharField(max_length=200, blank=True, null=True)
    data_compra = models.DateTimeField(default=timezone.now)
    data_entrega = models.DateTimeField(default=timezone.now)
    metodo_pagamento = models.CharField(max_length=200, blank=True, null=True)
    categoria_compra = models.CharField(max_length=200, blank=True, null=True)
    observacoes = models.CharField(max_length=200, blank=True, null=True)

    def save_purchase(self):
        self.data_compra = timezone.now

        self.save()

    def calcular_total(self):

        """
        Método que calcula o valor total dos produtos de uma compra.
        :return: Total de compras
        """

        i = Compra.objects.get(id_compra=self.id_compra).produtos.values('custo')
        for i in i:
            tot += float(i['custo'])
        pk = str(self.id_compra)
        Compra.objects.filter(id_compra=pk).update(total_produtos=tot)

    def calcular_produtos(self):
        """
        Método para calcular a quantidade de produtos em uma compra
        :return: quantidade de produtos para a tabela do BD
        """

        for i in self.itens_compra:
            self.qtd_produtos +=1

        self.save_purchase()

    def __str__(self):
        return 'Compra nº ' + str(self.id_compra)


class Produto(models.Model):
    """
    Esta classe cria os modelos para um produto de uma compra
    """
    __author__ = 'Giovane Pianco'
    __version__= '0.1'
    __email__ = 'gopianco@hotmail.com'
    __status__ = 'Development'
    __maintainer__ = 'Giovane Pianco'

    descricao = models.CharField(max_length=200)
    custo = models.DecimalField(max_digits=20, decimal_places=2)
    preco = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    peso = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    comprimento = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    largura = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    id_produto = models.AutoField(primary_key=True)
    status = models.CharField(max_length=40, blank=True, null=True)

    def save_product(self):
        self.save()

    def __str__(self):
        return self.descricao
