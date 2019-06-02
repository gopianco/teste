from django.shortcuts import render
from django.utils import timezone
from .models import Compra

def lista_compras(request):
    compras = Compra.objects.filter(data_compra__lte=timezone.now()).order_by('-data_compra')
    return render(request, 'compras/lista_compras.html', {'compras': compras})
