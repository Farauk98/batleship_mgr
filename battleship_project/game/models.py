# game/models.py

from django.db import models

class Board(models.Model):
    size = models.IntegerField(default=10)

    def __str__(self):
        return f'Board {self.id} - {self.size}x{self.size}'

class Ship(models.Model):
    board = models.ForeignKey(Board, related_name='ships', on_delete=models.CASCADE)
    start_x = models.IntegerField()
    start_y = models.IntegerField()
    end_x = models.IntegerField()
    end_y = models.IntegerField()

    def __str__(self):
        return f'Ship {self.id} on {self.board} from ({self.start_x}, {self.start_y}) to ({self.end_x}, {self.end_y})'

class Shot(models.Model):
    board = models.ForeignKey(Board, related_name='shots', on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.IntegerField()
    hit = models.BooleanField(default=False)

    def __str__(self):
        return f'Shot at ({self.x}, {self.y}) on {self.board} - {"Hit" if self.hit else "Miss"}'

class GameSession(models.Model):
    board = models.ForeignKey(Board, related_name='games', on_delete=models.CASCADE)
    strategy = models.CharField(max_length=255)
    moves = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'GameSession {self.id} - {self.strategy} - {"Completed" if self.completed else "In Progress"}'
