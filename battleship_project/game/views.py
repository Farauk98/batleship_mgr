# game/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Ship, GameSession
from .utils import place_ships_randomly, random_shooting_strategy

def create_board(request):
    board = Board.objects.create(size=10)
    ship_lengths = [2, 3, 4, 4, 5]
    place_ships_randomly(board, ship_lengths)
    return redirect('board_detail', board_id=board.id)

def index(request):
    boards = Board.objects.all()
    return render(request, 'index.html', {'boards': boards})

def board_detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    ships = board.ships.all()
    game_sessions = board.games.all()
    return render(request, 'board_detail.html', {'board': board, 'ships': ships, 'game_sessions': game_sessions})

def run_random_strategy(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    game_session = random_shooting_strategy(board)
    return redirect('game_session_detail', session_id=game_session.id)

def game_session_detail(request, session_id):
    game_session = get_object_or_404(GameSession, pk=session_id)
    shots = game_session.shots.all()
    return render(request, 'game_session_detail.html', {'game_session': game_session, 'shots': shots})
