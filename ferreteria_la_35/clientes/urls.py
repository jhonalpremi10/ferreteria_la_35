from django.urls import path
from . import views

urlpatterns = [
    # URL para listar clientes
    path('', views.cliente_list, name='cliente_list'),
    # URL para detalle de cliente
    path('<int:cliente_id>/', views.cliente_detail, name='cliente_detail'),
    # Otros URLs según sea necesario para CRUD de clientes, por ejemplo:
    # path('nuevo/', views.cliente_create, name='cliente_create'),
    # path('<int:cliente_id>/editar/', views.cliente_update, name='cliente_update'),
    # path('<int:cliente_id>/eliminar/', views.cliente_delete, name='cliente_delete'),
]

