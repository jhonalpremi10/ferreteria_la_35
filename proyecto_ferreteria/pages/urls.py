from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Asigna el nombre 'home' a la vista 'home'
    path('list/', views.page_list, name='page_list'),
    path('<int:page_id>/', views.page_detail, name='page_detail'),
    # Otras URLs aquí
]


