from django.shortcuts import render
from django.utils import timezone
from .models import Purchase

def purchase_list(request):
    purchases = Purchase.objects.filter(purchase_date__lte=timezone.now()).order_by('-purchase_date')
    return render(request, 'compras/purchase_list.html', {'purchases': purchases})
