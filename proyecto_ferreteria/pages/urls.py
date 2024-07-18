from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página de inicio
    path('list/', views.page_list, name='page_list'),  # Lista de páginas
    path('<int:page_id>/', views.page_detail, name='page_detail'),  # Detalle de página por ID
    # Otras URLs aquí
]


