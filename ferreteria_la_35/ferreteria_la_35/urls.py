"""
URL configuration for ferreteria_la_35 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view  # Importar la vista home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Añadir la ruta para la URL raíz
    path('accounts/', include('accounts.urls')),  # Incluir las URLs de la aplicación 'accounts'
    path('about/', include('about.urls')),  # Incluir las URLs de la aplicación 'about'
    path('pages/', include('pages.urls')),  # Incluir las URLs de la aplicación 'pages'
    path('productos/', include('productos.urls')),  # Incluir las URLs de la aplicación 'productos'
    path('clientes/', include('clientes.urls')),  # Incluir las URLs de la aplicación 'clientes'
=======

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
>>>>>>> b9b18d95c12427cd9661ca7a32aeae6a5b2e9c31
]



<<<<<<< HEAD

=======
>>>>>>> b9b18d95c12427cd9661ca7a32aeae6a5b2e9c31
