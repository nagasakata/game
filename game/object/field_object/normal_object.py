import pygame

from game.object.field_object.field_common import FieldCommon

class Road(FieldCommon):
    def __init__(self):
        self.color = pygame.Color(255,204,153)

        super().__init__(self.color)
