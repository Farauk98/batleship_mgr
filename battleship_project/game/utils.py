# game/utils.py

import random
from .models import Board, Ship, Shot, GameSession

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

def random_shooting_strategy(board):
    game_session = GameSession.objects.create(board=board, strategy="Random Shooting")
    size = board.size
    all_positions = [(x, y) for x in range(size) for y in range(size)]
    random.shuffle(all_positions)
    
    for x, y in all_positions:
        hit = False
        for ship in board.ships.all():
            if ship.start_x <= x <= ship.end_x and ship.start_y <= y <= ship.end_y:
                hit = True
                break
        Shot.objects.create(board=board, game_session=game_session, x=x, y=y, hit=hit)
        
        game_session.moves += 1
        if hit:
            game_session.save()
        
        # Check if all ships are hit
        if all_ships_sunk(board, game_session):
            game_session.completed = True
            game_session.save()
            break
    
    return game_session

def all_ships_sunk(board, game_session):
    for ship in board.ships.all():
        for x in range(ship.start_x, ship.end_x + 1):
            for y in range(ship.start_y, ship.end_y + 1):
                if not Shot.objects.filter(game_session=game_session, x=x, y=y, hit=True).exists():
                    return False
    return True
