from django.urls import path
from .views import page_list_view, page_detail_view

urlpatterns = [
    path('', page_list_view, name='page_list'),
    path('<int:page_id>/', page_detail_view, name='page_detail'),
]





