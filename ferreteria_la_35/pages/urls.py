from django.urls import path
from . import views

urlpatterns = [
    # URL para listar páginas
    path('', views.page_list, name='page_list'),
    # URL para detalle de página
    path('<int:page_id>/', views.page_detail, name='page_detail'),
]
