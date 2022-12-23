import pygame, copy

class CommonField():
    def __init__(self, field):
        self.field = field
        self.original_field = copy.copy(field)

    def set_field(self):
        self.field.blit(self.original_field, (0, 0))

        pygame.display.update()