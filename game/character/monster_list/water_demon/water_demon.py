import pygame
from game.character.about_status.level_experience_type import LevelExperienceType

from game.character.common.enemy import Enemy


class WaterDemon(Enemy):
    def __init__(self):
        super().__init__(name='water demon',
                         hp = 100, 
                         mp = 100,
                         attack = 10,
                         difence = 3,
                         magic_attack = 1,
                         magic_difence = 5,
                         speed = 1200,
                         skill={},
                         experiment=20,
                         level_experiment = LevelExperienceType().middle(),
                         image = pygame.image.load("game/character/monster_list/water_demon/water_demon.png").convert_alpha())