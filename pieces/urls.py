from django.urls import path
from . import views

urlpatterns = [
    path('', views.piece_index, name='piece_index'),
    path('<int:pk>/', views.piece_detail, name='piece_detail'),
]
