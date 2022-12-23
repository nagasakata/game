import pygame

from game.battle.spell import fire
from game.character.about_status.level_experience_type import LevelExperienceType
from game.character.common.human_common import Human

class Camila(Human):
    def __init__(self):
        self.status = {'hp':10000,
                       'mp':10000,
                       'attack':1000,
                       'difence':1000, 
                       'magic_attack':500, 
                       'magic_difence':500, 
                       'speed':1100}

        self.name = 'Camila'
        self.skill = {5:fire.Fire()}
        self.image = pygame.image.load("game/character/human_list/camila/camila_face.png").convert_alpha()
        self.level_experiment = LevelExperienceType().late_20()
        self.growth_type = [12, 8, 11, 8, 9, 4, 6]

        super().__init__(self.name, self.status, self.skill, self.level_experiment, self.image)
