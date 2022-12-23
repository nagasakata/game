import pygame
from game.character.about_status.level_experience_type import LevelExperienceType

from game.character.common.enemy import Enemy


class Slime(Enemy):
    def __init__(self):
        super().__init__(name='slime',
                         hp = 10000, 
                         mp = 10000,
                         attack = 500,
                         difence = 500,
                         magic_attack = 500,
                         magic_difence = 500,
                         speed = 1000,
                         skill={},
                         experiment = 2,
                         level_experiment = LevelExperienceType().early(),
                         image = pygame.image.load("game/character/monster_list/slime/slime.png").convert_alpha())