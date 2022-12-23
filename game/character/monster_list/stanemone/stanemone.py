import pygame
from game.character.about_status.level_experience_type import LevelExperienceType

from game.character.common.enemy import Enemy


class Stanemone(Enemy):
    def __init__(self):
        super().__init__(name='stanemone',
                         hp = 100, 
                         mp = 100,
                         attack = 10,
                         difence = 3,
                         magic_attack = 1,
                         magic_difence = 5,
                         speed = 300,
                         skill={},
                         experiment=5,
                         level_experiment = LevelExperienceType().early(),
                         image = pygame.image.load("game/character/monster_list/stanemone/stanemone.png").convert_alpha())