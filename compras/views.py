from django.shortcuts import render

def purchase_list(request):
    return render(request, 'compras/purchase_list.html', {})
