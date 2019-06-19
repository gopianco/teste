from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user,),
    path('logout', views.logout_user),
    path('login/submit', views.submit_login),
    path('', views.lista_compras, name='lista_compras'),
    path('compra/<int:pk>/', views.compra_detalhes, name='compra_detalhes'),
    path('compra/new', views.nova_compra, name='nova_compra'),
    path('compra/<int:pk>/editar/', views.editar_compra, name='editar_compra'),
    path('compra/<int:pk>/remover', views.remover_compra, name='remover_compra'),

]
