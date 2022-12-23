import pygame

from game.battle.spell import fire
from game.character.about_status.level_experience_type import LevelExperienceType
from game.character.common.human_common import Human

class Emma(Human):
    def __init__(self):
        self.status = {'hp':5000,
                       'mp':20000,
                       'attack':500,
                       'difence':500, 
                       'magic_attack':1000, 
                       'magic_difence':1000, 
                       'speed':100}

        self.name = 'Emma'
        self.skill = {5:fire.Fire()}
        self.image = pygame.image.load("game/character/human_list/emma/emma_face.png").convert_alpha()
        self.level_experiment = LevelExperienceType().late_20()

        super().__init__(self.name, self.status, self.skill, self.level_experiment, self.image)
