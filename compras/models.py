from django.db import models
from django.utils import timezone

metodo_envio = (
    ('0414', 'SEDEX'),
    ('04510', 'PAC'),
    ('0215', 'SEDEX10'),
)


class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    data_compra = models.DateTimeField(default=timezone.now)
    codigo_rastreio = models.CharField(max_length=40, blank=True, null=True)
    total_compra = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    metodo_envio = models.CharField(max_length=6, choices=metodo_envio, blank=True, null=True)
    tempo_envio = models.CharField(max_length=2, blank=True, null=True)
    produtos = models.ManyToManyField('Produto')
    
    def save_purchase(self):
        self.data_compra = timezone.now
        
        self.save()

    def calcular_total(self) :
        i = Compra.objects.get(id_compra = self.id_compra).produtos.values('custo')
        for i in i:
            tot += float(i['custo'])
        pk = str(self.id_compra)    
        Compra.objects.filter(id_compra = pk).update(total_compra=tot)     

    def __str__(self):
       return 'Compra nº ' + str(self.id_compra)
    

class Produto(models.Model):
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

