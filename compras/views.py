from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import ComprarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Compra


def login_user(request):
    return render(request, 'compras/login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválidos')

    return redirect('/')

@login_required(login_url='/login')
def lista_compras(request):
    compras = Compra.objects.filter(data_compra__lte=timezone.now()).order_by('-data_compra')
    
    return render(request, 'compras/lista_compras.html', {'compras': compras})

def compra_detalhes(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    prod = Compra.objects.get(id_compra=pk)
    outro = prod.produtos.all()
    return render(request, 'compras/compra_detalhes.html', {'compra': compra, 'produtos': outro})

@login_required(login_url='/login')
def nova_compra(request):
    if request.method == 'POST':
        form = ComprarForm(request.POST)
        if form.is_valid():
            compra = form.save()
            
            tot = 0.0

            i = Compra.objects.get(id_compra=compra.pk).produtos.values('custo')
            for i in i:
                tot += float(i['custo'])
            
            compra.total_produtos = tot
            compra.save()
            return redirect('compra_detalhes', pk=compra.pk)
    else:
        form = ComprarForm()
    return render(request, 'compras/editar_compra.html', {'form': form})

@login_required(login_url='/login')
def editar_compra(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    if request.method == 'POST':
        form = ComprarForm(request.POST, instance=compra)
        if form.is_valid():
            compra = form.save()
            
            tot = 0.0

            i = Compra.objects.get(id_compra = compra.pk).produtos.values('custo')
            for i in i:
                tot += float(i['custo'])
            
            compra.total_produtos = tot
            compra.save()
            return redirect('compra_detalhes', pk=compra.pk)
    else:
        form = ComprarForm(instance=compra)

    return render(request, 'compras/editar_compra.html', {'form': form})

@login_required(login_url='/login')
def remover_compra(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    delete = Compra.objects.filter(id_compra = compra.pk).delete()

    return redirect('/')

