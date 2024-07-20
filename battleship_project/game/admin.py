from django.contrib import admin

from .models import Board, Ship, Shot, GameSession

admin.site.register(Board)
admin.site.register(Ship)
admin.site.register(Shot)
admin.site.register(GameSession)