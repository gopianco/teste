from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_compras, name='lista_compras'),
    path('compra/<int:pk>/', views.compra_detalhes, name='compra_detalhes'),
]
