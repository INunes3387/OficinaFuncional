from django.urls import path

from oficina.views import *

urlpatterns = [
    path('', list_orcamento, name='list_orcamento'),
    path('new', create_orcamento, name='create_orcamento'),
    path('update/<int:id>/', update_orcamento, name='update_orcamento'),
    path('delete/<int:id>/', delete_orcamento, name='delete_orcamento'),
    path('newCliente', create_cliente, name='create_cliente'),
]


