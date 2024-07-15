from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
    path('<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('blog/', views.blog_index, name='blog_index'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
]
