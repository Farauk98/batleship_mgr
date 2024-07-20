# game/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Ship
from .utils import place_ships_randomly

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
    return render(request, 'board_detail.html', {'board': board, 'ships': ships})
