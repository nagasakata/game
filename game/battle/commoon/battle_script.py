import sys
import pygame
import copy
from pygame.locals import *
from game.battle.commoon.attack import Attack
from game.character.common.enemy import Enemy
from game.character.common.friend import Friend

from game.character.common.friend_member import Member

class BattleScript():
    def __init__(self, screen, field, member) -> None:
        self.screen = screen
        self.original_screen = copy.copy(self.screen)
        self.member = member
        self.field = field
        self.action_order = []
        self.turn_count = 1
        self.finish = True #逃げた場合、もしくは戦闘そのものがおわった場合False
        self.fin = False #一人のターンが終わったときTrue
        self.done = False #何か画面に変化があるときTrue
        self.cursor_count = 1
        self.experiment_all = 0

# 画面に変化がある時呼ぶ
    def make_original(self):

        self.screen.fill((0, 0, 0))
        pygame.draw.line(self.screen, (255, 255, 255), (0, 600), (1500, 600))
        pygame.draw.line(self.screen, (255, 255, 255), (400, 0), (400, 900))
        pygame.draw.line(self.screen, (255, 255, 255), (0, 150), (400, 150))
        pygame.draw.line(self.screen, (255, 255, 255), (0, 300), (400, 300))
        pygame.draw.line(self.screen, (255, 255, 255), (0, 450), (400, 450))

        self.font = pygame.font.Font("ipaexg.ttf", 30)

        for i in self.member.member:
            text_name = self.font.render(self.member.member[i].get_name(), True, (255, 255, 255))
            text_hp = self.font.render("HP: " + str(self.member.member[i].get_hp()), True, (255, 255, 255))
            text_mp = self.font.render("MP: " + str(self.member.member[i].get_mp()), True, (255, 255, 255))
            self.screen.blit(text_name, (50, 10 + i * 150))
            self.screen.blit(text_hp, (50, 55 + i * 150))
            self.screen.blit(text_mp, (50, 100 + i * 150))
            self.member.member[i].draw_image(self.screen, 300, 75 + i * 150)

        text_attack = self.font.render("こうげき", True, (255, 255, 255))
        text_skill = self.font.render("こうどう", True, (255, 255, 255))
        text_item = self.font.render("アイテム", True, (255, 255, 255))
        text_run = self.font.render("にげる", True, (255, 255, 255))
        self.screen.blit(text_attack, (250, 625))
        self.screen.blit(text_skill, (250, 665))
        self.screen.blit(text_item, (250, 705))
        self.screen.blit(text_run, (250, 745))

        self.enemies = self.field.enemy_member

        self.enemy_print()

        self.original_battle = copy.copy(self.screen)
        pygame.display.update()

    def battle(self):
        self.make_original()

        self.make_action_order(self.member.member, self.enemies.enemies)
        font2 = pygame.font.Font("ipaexg.ttf", 60)
        self.turn_count = 1

        while True:
            if not self.finish:
                break
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if not self.finish:
                        break
                    if event.key == K_a:
                        for turn in self.action_order:
                            if self.finish:
                                self.done = False
                                self.fin = False
                                if isinstance(turn, Friend):
                                    self.friend_turn(turn)
                                elif isinstance(turn, Enemy):
                                    self.enemy_turn(turn)
                                if self.done:
                                    self.make_original()
                                self.screen.blit(self.original_battle, (0, 0))
                                if len(self.enemies.enemies) == 0:
                                    print("you win!")
                                    self.member.win_experiment(self.experiment_all)
                                    self.finish = False
                                elif len(self.member.member) == 0:
                                    print("you lose")
                                    self.finish = False
                            else:
                                break
                        else:
                            continue
                        break
                    self.turn_count = self.turn_count + 1
                    self.screen.blit(self.original_battle, (0, 0))
            else:
                continue
            break
                

    def enemy_print(self):
        enemy_many = len(self.enemies.enemies)
        for enemy_id in self.enemies.enemies:
            enemy_size = self.enemies.enemies[enemy_id].get_image_size()
            text_name = self.font.render(self.enemies.enemies[enemy_id].get_name(), True, (255, 255, 255))
            text_hp = self.font.render("HP: " + str(self.enemies.enemies[enemy_id].get_hp()), True, (255, 255, 255))
            if enemy_many == 1:
                self.enemies.enemies[enemy_id].draw_image(self.screen, 930, 300)
                self.screen.blit(text_name, (880, 310 + enemy_size[1]))
                self.screen.blit(text_hp, (880, 350 + enemy_size[1]))
            elif enemy_many == 2:
                self.enemies.enemies[enemy_id].draw_image(self.screen, 320 + enemy_id * 400, 300)
                self.screen.blit(text_name, (270 + enemy_id * 400, 310 + enemy_size[1]))
                self.screen.blit(text_hp, (270 + enemy_id * 400, 350 + enemy_size[1]))
            elif enemy_many == 3:
                self.enemies.enemies[enemy_id].draw_image(self.screen, 320 + enemy_id * 300, 300)
                self.screen.blit(text_name, (270 + enemy_id * 300, 310 + enemy_size[1]))
                self.screen.blit(text_hp, (270 + enemy_id * 300, 350 + enemy_size[1]))
            elif enemy_many == 4:
                if enemy_id <= 2:
                    self.enemies.enemies[enemy_id].draw_image(self.screen, 410 + enemy_id * 400, 150)
                    self.screen.blit(text_name, (360 + enemy_id * 400, 160 + enemy_size[1]))
                    self.screen.blit(text_hp, (360 + enemy_id * 400, 200 + enemy_size[1]))
                else:
                    self.enemies.enemies[enemy_id].draw_image(self.screen, 610 + (enemy_id - 3) * 400, 390)
                    self.screen.blit(text_name, (560 + (enemy_id - 3) * 400, 400 + enemy_size[1]))
                    self.screen.blit(text_hp, (560 + (enemy_id - 3) * 400, 440 + enemy_size[1]))
            elif enemy_many == 5:
                if enemy_id <= 2:
                    self.enemies.enemies[enemy_id].draw_image(self.screen, 320 + enemy_id * 400, 150)
                    self.screen.blit(text_name, (270 + enemy_id * 400, 160 + enemy_size[1]))
                    self.screen.blit(text_hp, (270 + enemy_id * 400, 200 + enemy_size[1]))
                else:
                    self.enemies.enemies[enemy_id].draw_image(self.screen, 250 + (enemy_id - 2) * 350, 390)
                    self.screen.blit(text_name, (170 + (enemy_id - 2) * 350, 400 + enemy_size[1]))
                    self.screen.blit(text_hp, (170 + (enemy_id - 2) * 350, 440 + enemy_size[1]))


    def make_action_order(self, f_member:dict, e_member:dict):
        self.action_order = []
        for e in e_member:
            pre_order = []
            count = 1
            if len(self.action_order) == 0:
                self.action_order.append(e_member[e])
            else:
                for i in self.action_order:
                    if count == (len(self.action_order)):
                        pre_order.append(i)
                        if i.get_speed() >= e_member[e].get_speed():
                            self.action_order = pre_order + [e_member[e]]
                        else:
                            self.action_order = pre_order[0:count-1] + [e_member[e]] + pre_order[-1:]

                    elif i.get_speed() <= e_member[e].get_speed():
                        self.action_order = pre_order + [e_member[e]] + self.action_order[-(len(self.action_order) - count + 1):]
                        break
                    else:
                        pre_order.append(i)
                        count = count + 1

        for f in f_member:
            pre_order = []
            count = 1
            for i in self.action_order:
                if count == (len(self.action_order)):
                    pre_order.append(i)
                    if i.get_speed() >= f_member[f].get_speed():
                        self.action_order = pre_order + [f_member[f]]
                    else:
                        self.action_order = pre_order[0:count-1] + [f_member[f]] + pre_order[-1:]
                elif i.get_speed() <= f_member[f].get_speed():
                    self.action_order = pre_order + [f_member[f]] + self.action_order[-(len(self.action_order) - count + 1):]
                    break
                else:
                    pre_order.append(i)
                    count = count + 1

        return self.action_order

    def enemy_turn(self, turn):
        text_start = self.font.render(turn.get_name(), True, (255, 255, 255))
        self.screen.blit(text_start, (48,625))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_a:
                        break
            else:
                continue
            break

    def friend_turn(self, turn):
        turn.draw_image(self.screen, 100, 720)
        friend_turn_original = copy.copy(self.screen)
        cursor = self.font.render("->", True, (255, 255, 255))
        cursor_y = 625
        self.screen.blit(cursor, (200, cursor_y))
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.screen.blit(friend_turn_original, (0, 0))
                        if cursor_y == 625:
                            cursor_y = 745
                        else:
                            cursor_y = cursor_y - 40
                        self.screen.blit(cursor, (200, cursor_y))
                    elif event.key == K_DOWN:
                        self.screen.blit(friend_turn_original, (0, 0))
                        if cursor_y == 745:
                            cursor_y = 625
                        else:
                            cursor_y = cursor_y + 40
                        self.screen.blit(cursor, (200, cursor_y))
                    elif event.key == K_a:
                        if cursor_y == 625:
                            self.attack(turn)
                        elif cursor_y == 665:
                            self.use_skill()
                        elif cursor_y == 705:
                            self.use_item()
                        elif cursor_y == 745:
                            self.run_away()

                    if self.fin:
                        break
            else:
                continue
            break

    def attack(self, turn_player):
        original_attack = copy.copy(self.screen)
        self.cursor_count = 1
        enemy_many = len(self.enemies.enemies)
        self.display_cursor_initial(enemy_many)
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.display_cursor(enemy_many, K_RIGHT, original_attack)
                    elif event.key == K_LEFT:
                        self.display_cursor(enemy_many, K_LEFT, original_attack)
                    elif event.key == K_a:
                        attack_script = Attack(turn_player, self.enemies.enemies[self.cursor_count])
                        if attack_script.do_attack():
                            self.experiment_all = self.experiment_all + self.enemies.enemies[self.cursor_count].get_experiment()
                            self.enemies.kill_enemy(self.enemies.enemies[self.cursor_count])
                        self.done = True
                        self.fin = True
                        break
                    elif event.key == K_q:
                        break
            else:
                continue
            break
        self.screen.blit(original_attack, (0, 0))

    def display_cursor_initial(self, enemy_many):
        cursor = self.font.render("→", True, (255, 255, 255))
        enemy_size = self.enemies.enemies[1].get_image_size()
        if enemy_many == 1:
            self.screen.blit(cursor, (830, 310 + enemy_size[1]))
        elif enemy_many == 2:
            self.screen.blit(cursor, (620, 310 + enemy_size[1]))
        elif enemy_many == 3:
            self.screen.blit(cursor, (520, 310 + enemy_size[1]))
        elif enemy_many == 4:
            self.screen.blit(cursor, (710, 160 + enemy_size[1]))
        elif enemy_many == 5:
            self.screen.blit(cursor, (620, 160 + enemy_size[1]))

    def display_cursor(self, enemy_many:int, key, original):
        self.screen.blit(original, (0, 0))
        cursor = self.font.render("→", True, (255, 255, 255))
        if enemy_many == 1:
            enemy_size = self.enemies.enemies[1].get_image_size()
            self.screen.blit(cursor, (830, 310 + enemy_size[1]))
        elif enemy_many == 2:
            if self.cursor_count == 2:
                self.cursor_count = self.cursor_count - 1
                enemy_size = self.enemies.enemies[self.cursor_count].get_image_size()
                self.screen.blit(cursor, (620, 310 + enemy_size[1]))
            else:
                self.cursor_count = self.cursor_count + 1
                enemy_size = self.enemies.enemies[self.cursor_count].get_image_size()
                self.screen.blit(cursor, (1020, 310 + enemy_size[1]))
        elif enemy_many == 3:
            if key == K_LEFT:
                if self.cursor_count == 1:
                    self.cursor_count = 3
                else:
                    self.cursor_count = self.cursor_count - 1
                enemy_size = self.enemies.enemies[self.cursor_count].get_image_size()
                self.screen.blit(cursor, (220 + self.cursor_count * 300, 310 + enemy_size[1]))
            elif key == K_RIGHT:
                if self.cursor_count == 3:
                    self.cursor_count = 1
                else:
                    self.cursor_count = self.cursor_count + 1
                enemy_size = self.enemies.enemies[self.cursor_count].get_image_size()
                self.screen.blit(cursor, (220 + self.cursor_count * 300, 310 + enemy_size[1]))
        elif enemy_many == 4:
            if key == K_LEFT:
                if self.cursor_count == 1:
                    self.cursor_count = 4
                else:
                    self.cursor_count = self.cursor_count - 1
            elif key == K_RIGHT:
                if self.cursor_count == 4:
                    self.cursor_count = 1
                else:
                    self.cursor_count = self.cursor_count + 1
            enemy_size = self.enemies.enemies[self.cursor_count].get_image_size()
            if self.cursor_count <= 2:
                self.screen.blit(cursor, (310 + self.cursor_count * 400, 160 + enemy_size[1]))
            else:
                self.screen.blit(cursor, (510 + (self.cursor_count - 3) * 400, 400 + enemy_size[1]))
        elif enemy_many == 5:
            if key == K_LEFT:
                if self.cursor_count == 1:
                    self.cursor_count = 5
                else:
                    self.cursor_count = self.cursor_count - 1
            elif key == K_RIGHT:
                if self.cursor_count == 5:
                    self.cursor_count = 1
                else:
                    self.cursor_count = self.cursor_count + 1
            enemy_size = self.enemies.enemies[self.cursor_count].get_image_size()
            if self.cursor_count <= 2:
                self.screen.blit(cursor, (220 + self.cursor_count * 400, 160 + enemy_size[1]))
            else:
                self.screen.blit(cursor, (120 + (self.cursor_count - 2) * 350, 400 + enemy_size[1]))
        


    def use_skill(self):
        pass

    def use_item(self):
        pass

    def run_away(self):
        self.finish = False
        self.fin = True


