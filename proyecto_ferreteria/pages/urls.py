# pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pages/', views.page_list, name='page_list'),
    path('pages/<int:page_id>/', views.page_detail, name='page_detail'),
]