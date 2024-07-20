# game/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('board/<int:board_id>/', views.board_detail, name='board_detail'),
    path('create_board/', views.create_board, name='create_board'),
]
