from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Compra
from .forms import ComprarForm

def lista_compras(request):   
    compras = Compra.objects.filter(data_compra__lte=timezone.now()).order_by('-data_compra')
    
    return render(request, 'compras/lista_compras.html', {'compras': compras})

def compra_detalhes(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    prod = Compra.objects.get(id_compra=pk)
    outro = prod.produtos.all()
    return render(request, 'compras/compra_detalhes.html', {'compra': compra, 'produtos': outro})

def nova_compra(request):
    if request.method == 'POST':
        form = ComprarForm(request.POST)
        if form.is_valid():
            compra = form.save()
            
            tot = 0.0

            i = Compra.objects.get(id_compra = compra.pk).produtos.values('custo')
            for i in i:
                tot += float(i['custo'])
            
            compra.total_compra = tot
            compra.save()
            return redirect('compra_detalhes', pk=compra.pk)
    else:
        form = ComprarForm()
    return render(request, 'compras/editar_compra.html', {'form': form})

