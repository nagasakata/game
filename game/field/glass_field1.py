import pygame

from game.field.common_field import CommonField
from game.object.field_object.encount_object import EncountGlass, EncountSwamp
from game.object.field_object.normal_object import Road
from game.object.field_object.unenter_object import BigRock, Lake


class GlassField1(CommonField):
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0))
        self.screen.fill((153,255,50))
        
        road = Road()
        road.draw(self.screen, 400, 0, 200, 900)

        glass = EncountGlass()
        glass.draw(self.screen, 700, 0, 750, 300)

        swamp = EncountSwamp()
        swamp.draw(self.screen, 700, 500, 750, 400)

        lake = Lake()
        lake.draw(self.screen, 0, 0, 200, 900)


        super().__init__(self.screen)

    def get_screen(self):
        return self.screen