from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
    path('<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('blog/', views.blog_index, name='blog_index'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
]
<<<<<<< HEAD
=======

>>>>>>> b9b18d95c12427cd9661ca7a32aeae6a5b2e9c31
