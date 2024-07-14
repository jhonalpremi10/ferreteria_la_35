from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('registro/', views.signup, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('perfil/', views.profile, name='perfil'),
]
