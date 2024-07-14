# En pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('listar-productos/', views.listar_productos, name='listar_productos'),
   
]
