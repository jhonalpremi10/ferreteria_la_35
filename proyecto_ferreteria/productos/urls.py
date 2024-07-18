# productos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('productos/nuevo/', views.nuevo_producto, name='nuevo_producto'),
    path('productos/<int:producto_id>/editar/', views.editar_producto, name='editar_producto'),
    path('productos/<int:producto_id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
]

