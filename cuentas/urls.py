from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_usuario, name='login'),
    path('profile/', views.profile, name='perfil'),
    path('about/', views.about, name='about'),
]

