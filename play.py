import pygame

from game.field.glass_field1 import GlassField1
from game.object.player_object.player import Player

pygame.init()

g = GlassField1()

g.set_field()

me = Player(g.get_screen())

me.move()