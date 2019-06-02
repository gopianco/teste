from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Compra

def lista_compras(request):
    compras = Compra.objects.filter(data_compra__lte=timezone.now()).order_by('-data_compra')
    return render(request, 'compras/lista_compras.html', {'compras': compras})

def compra_detalhes(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    prod = Compra.objects.get(id_compra=pk)
    outro = prod.produtos.all()
    return render(request, 'compras/compra_detalhes.html', {'compra': compra, 'produtos': outro})
