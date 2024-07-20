# game/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('board/<int:board_id>/', views.board_detail, name='board_detail'),
    path('create_board/', views.create_board, name='create_board'),
    path('board/<int:board_id>/run_random_strategy/', views.run_random_strategy, name='run_random_strategy'),
    path('game_session/<int:session_id>/', views.game_session_detail, name='game_session_detail'),
]
