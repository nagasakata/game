import pygame
from pygame.locals import *
import sys, copy, random
from game.battle.commoon.battle_script import BattleScript
from game.character.about_status.level_experience_type import LevelExperienceType
from game.character.common.friend import Friend
from game.character.common.friend_member import Member
from game.character.human_list.olivia.olivia import Olivia
from game.character.human_list.emma.emma import Emma
from game.character.human_list.camila.camila import Camila
from game.character.human_list.riley.riley import Riley
from game.character.monster_list.killermush.killermush import Killermush

from game.object.field_object.encount_object import EncountGlass, EncountObject
from game.object.field_object.unenter_object import UnenterObject
from game.object.system_object.menu import Menu

class Player():
    def __init__(self, screen) -> None:
        self.me_surface = pygame.image.load("game/object/player_object/main_front.png").convert_alpha()
        self.me = self.me_surface.get_rect()
        self.me.center = (500, 50)
        self.screen = screen
        self.original_screen = copy.copy(screen)
        self.member = Member()
        self.member.add_member(Friend(Camila()))
        self.member.add_member(Friend(Emma()))
        self.member_all = []
        self.item = []
        self.menu = Menu(self.screen, self.member, self.member_all, self.item)
        
    def get_surface(self):
        return self.me_surface

    def get_dest(self):
        return self.me

    def move(self):

        clock = pygame.time.Clock()

        while True:
            clock.tick(30)
            self.draw()
            pygame.display.update()
            self.key_handler()


    def draw(self):
        self.screen.blit(self.original_screen, (0, 0))
        self.screen.blit(self.get_surface(), self.get_dest())

    def key_handler(self):

        unenter_object = UnenterObject()
        self.me_bottomleft = self.me.bottomleft
        self.me_bottomright = self.me.bottomright
        self.me_topleft = (self.me.bottomleft[0], 2 * self.me.centery - self.me.bottom)
        self.me_topright = (self.me.bottomright[0], 2 * self.me.centery - self.me.bottom)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_w]:
            menu_display = self.menu.indicate()
            self.screen.blit(menu_display, (0, 0))
        elif pressed_keys[K_a]:
            pass
        else:
            if pressed_keys[K_RIGHT]:
                self.me_surface = pygame.image.load("game/object/player_object/main_right.png").convert_alpha()
                if (not self.original_screen.get_at(self.me_topright) in unenter_object.get_unenter_color_list()) & (not self.original_screen.get_at(self.me_bottomright) in unenter_object.get_unenter_color_list()):
                    if pressed_keys[K_d]:
                        self.me.move_ip(9, 0)
                    else:
                        self.me.move_ip(3, 0)
                self.encount()
            if pressed_keys[K_LEFT]:
                self.me_surface = pygame.image.load("game/object/player_object/main_left.png").convert_alpha()
                if (not self.original_screen.get_at(self.me_topleft) in unenter_object.get_unenter_color_list()) & (not self.original_screen.get_at(self.me_bottomleft) in unenter_object.get_unenter_color_list()):
                    if pressed_keys[K_d]:
                        self.me.move_ip(-9, 0)
                    else:
                        self.me.move_ip(-3, 0)
                self.encount()
            if pressed_keys[K_UP]:
                self.me_surface = pygame.image.load("game/object/player_object/main_back.png").convert_alpha()
                if (not self.original_screen.get_at(self.me_topleft) in unenter_object.get_unenter_color_list()) & (not self.original_screen.get_at(self.me_topright) in unenter_object.get_unenter_color_list()):
                    if pressed_keys[K_d]:
                        self.me.move_ip(0, -9)
                    else:
                        self.me.move_ip(0, -3)
                self.encount()
            if pressed_keys[K_DOWN]:
                self.me_surface = pygame.image.load("game/object/player_object/main_front.png").convert_alpha()
                if (not self.original_screen.get_at(self.me_bottomleft) in unenter_object.get_unenter_color_list()) & (not self.original_screen.get_at(self.me_bottomright) in unenter_object.get_unenter_color_list()):
                    if pressed_keys[K_d]:
                        self.me.move_ip(0, 9)
                    else:
                        self.me.move_ip(0, 3)
                self.encount()

    def encount(self):
        encount_object = EncountObject()
        now_color = self.original_screen.get_at(self.me.center)
        if now_color in encount_object.get_encount_object_color():
            i = random.randint(1, 10)
            if i == 1:
                now_field = encount_object.color_field(now_color)
                battle_start = BattleScript(self.screen, now_field, self.member)
                battle_start.battle()
                


