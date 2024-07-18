from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # Registro de usuario
    path('login/', views.login_view, name='login'),  # Inicio de sesión
    # Otras URLs aquí
]



