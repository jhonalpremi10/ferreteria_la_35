# cuentas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('perfil/', views.perfil, name='perfil'),
]
