# game/utils.py

import random
from .models import Board, Ship

def can_place_ship(board, start_x, start_y, length, direction):
    size = board.size
    if direction == "horizontal":
        if start_y + length > size:
            return False
        for i in range(length):
            if Ship.objects.filter(board=board, start_x=start_x, start_y=start_y + i).exists():
                return False
    else:
        if start_x + length > size:
            return False
        for i in range(length):
            if Ship.objects.filter(board=board, start_x=start_x + i, start_y=start_y).exists():
                return False
    return True

def place_ship(board, start_x, start_y, length, direction):
    if direction == "horizontal":
        for i in range(length):
            Ship.objects.create(board=board, start_x=start_x, start_y=start_y + i, end_x=start_x, end_y=start_y + i)
    else:
        for i in range(length):
            Ship.objects.create(board=board, start_x=start_x + i, start_y=start_y, end_x=start_x + i, end_y=start_y)

def place_ships_randomly(board, ship_lengths):
    size = board.size
    for length in ship_lengths:
        placed = False
        while not placed:
            start_x = random.randint(0, size - 1)
            start_y = random.randint(0, size - 1)
            direction = random.choice(["horizontal", "vertical"])
            if can_place_ship(board, start_x, start_y, length, direction):
                place_ship(board, start_x, start_y, length, direction)
                placed = True
