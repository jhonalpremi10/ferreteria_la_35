from django.urls import path
from . import views

urlpatterns = [
    path('', views.cliente_list, name='cliente_list'),
    path('<int:cliente_id>/', views.cliente_detail, name='cliente_detail'),
]
