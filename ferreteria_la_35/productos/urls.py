from django.urls import path
from . import views

urlpatterns = [
    path('pages/', views.blog_index, name='blog_index'),
    path('pages/<int:post_id>/', views.blog_detail, name='blog_detail'),
    # Otras rutas
    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('detalle_producto/<int:id>/', views.detalle_producto, name='detalle_producto'),
]

