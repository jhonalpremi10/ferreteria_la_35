# AppCoder/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('cursoFormulario/', views.cursoFormulario, name='CursoFormulario'),
    path('busquedaCamada/', views.busquedaCamada, name='BusquedaCamada'),
    path('buscar/', views.buscar, name='Buscar'),
]
