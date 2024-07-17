from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_list, name='page_list'),
    path('<int:page_id>/', views.page_detail, name='page_detail'),
]


