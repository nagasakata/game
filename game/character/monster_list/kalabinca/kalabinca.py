import pygame
from game.character.about_status.level_experience_type import LevelExperienceType

from game.character.common.enemy import Enemy


class Kalabinca(Enemy):
    def __init__(self):
        super().__init__(name='kalabinca',
                         hp = 5000, 
                         mp = 1000,
                         attack = 1000,
                         difence = 300,
                         magic_attack = 100,
                         magic_difence = 500,
                         speed = 300,
                         skill={},
                         experiment=10,
                         level_experiment = LevelExperienceType().middle(),
                         image = pygame.image.load("game/character/monster_list/kalabinca/kalabinca.png").convert_alpha())