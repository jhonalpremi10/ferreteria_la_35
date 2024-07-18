from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),  # URL para la lista de productos
    path('<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('nuevo/', views.nuevo_producto, name='nuevo_producto'),
    path('<int:producto_id>/editar/', views.editar_producto, name='editar_producto'),
    path('<int:producto_id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
]


