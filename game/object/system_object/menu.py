import pygame, copy
from pygame.locals import *
import sys


class Menu():

    def __init__(self, screen, member, all_member = list, item = list):
        self.screen = screen
        self.original_screen = copy.copy(screen)
        self.member = member
        self.all_member = all_member
        self.item = item
        self.font = pygame.font.Font("ipaexg.ttf", 30)

    def indicate(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (50, 50, 230, 450))
        
        text_a = self.font.render('パーティー', True, (255, 255, 255))
        text_b = self.font.render('アイテム', True, (255, 255, 255))
        text_c = self.font.render('なにか', True, (255, 255, 255))
        text_d = self.font.render('セーブ', True, (255, 255, 255))
        cursor = self.font.render('->', True, (255, 255, 255))

        self.screen.blit(text_a, (110, 110))
        self.screen.blit(text_b, (110, 210))
        self.screen.blit(text_c, (110, 310))
        self.screen.blit(text_d, (110, 410))
        self.original_menu = copy.copy(self.screen)
        cursor_y = 110
        self.screen.blit(cursor, (65, cursor_y))

        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        self.screen.blit(self.original_menu, (0,0))
                        if cursor_y == 410:
                            cursor_y = 110
                            self.screen.blit(cursor, (65, cursor_y))
                        else:
                            cursor_y = cursor_y + 100
                            self.screen.blit(cursor, (65, cursor_y))
                    elif event.key == K_UP:
                        self.screen.blit(self.original_menu, (0,0))
                        if cursor_y == 110:
                            cursor_y = 410
                            self.screen.blit(cursor, (65, cursor_y))
                        else:
                            cursor_y = cursor_y - 100
                            self.screen.blit(cursor, (65, cursor_y))
                    elif (event.key == K_RIGHT) | (event.key == K_a):
                        if cursor_y == 110:
                            self.party_menu()
                        elif cursor_y == 210:
                            self.item_menu()
                        elif cursor_y == 310:
                            self.any_menu()
                        elif cursor_y == 410:
                            self.save_menu()
                        self.screen.blit(self.original_menu, (0, 0))
                        self.screen.blit(cursor, (65, cursor_y))

                    if (event.key == K_LEFT) | (event.key == K_q):
                        break
            else:
                pygame.display.update()
                continue
            break

        return self.original_screen

    def party_menu(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (300, 110, 320, 350))
        text_a = self.font.render('パーティーの情報', True, (255, 255, 255))
        text_b = self.font.render('パーティーの変更', True, (255, 255, 255))
        text_c = self.font.render('パーティー', True, (255, 255, 255))
        cursor = self.font.render('->', True, (255, 255, 255))
        cursor_y = 170

        self.screen.blit(text_a, (360, 170))
        self.screen.blit(text_b, (360, 270))
        self.screen.blit(text_c, (360, 370))
        original_menu = copy.copy(self.screen)
        self.screen.blit(cursor, (315, cursor_y))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.screen.blit(original_menu, (0, 0))
                        if cursor_y == 170:
                            self.screen.blit(cursor, (315, 370))
                            cursor_y = 370
                        else:
                            self.screen.blit(cursor, (315, cursor_y - 100))
                            cursor_y = cursor_y - 100
                    elif event.key == K_DOWN:
                        self.screen.blit(original_menu, (0, 0))
                        if cursor_y == 370:
                            self.screen.blit(cursor, (315, 170))
                            cursor_y = 170
                        else:
                            self.screen.blit(cursor, (315, cursor_y + 100))
                            cursor_y = cursor_y + 100
                    elif (event.key == K_RIGHT) | (event.key == K_a):
                        if cursor_y == 170:
                            self.party_info()
                        elif cursor_y == 270:
                            pass
                        elif cursor_y == 370:
                            pass
                        self.screen.blit(original_menu, (0, 0))
                        self.screen.blit(cursor, (315, cursor_y))
                    elif (event.key == K_LEFT) | (event.key == K_q):
                        break
            else:
                pygame.display.update()
                continue
            break

    def party_info(self):
        member_size = len(self.member.member)
        pygame.draw.rect(self.screen, (0, 0, 0), (640, 170, 200, 60 + (member_size - 1)* 50))
        for i in self.member.member:
            text_member = self.font.render(self.member.member[i].get_name(), True, (255, 255, 255))
            self.screen.blit(text_member, (700, 180 + i * 50))
        original_menu = copy.copy(self.screen)
        cursor = self.font.render('->', True, (255, 255, 255))
        cursor_y = 180
        self.screen.blit(cursor, (655, 180))
        self.one_info((cursor_y - 180) / 50)

        pygame.display.update()
        
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.screen.blit(original_menu, (0, 0))
                        if cursor_y == 180:
                            self.screen.blit(cursor, (655, 180 + (member_size - 1) * 50))
                            cursor_y = 180 + (member_size - 1) * 50
                        else:
                            self.screen.blit(cursor, (655, cursor_y - 50))
                            cursor_y = cursor_y - 50
                        self.one_info((cursor_y - 180) / 50)
                    elif event.key == K_DOWN:
                        self.screen.blit(original_menu, (0, 0))
                        if cursor_y == 180 + (member_size - 1) * 50:
                            self.screen.blit(cursor, (655, 180))
                            cursor_y = 180
                        else:
                            self.screen.blit(cursor, (655, cursor_y + 50))
                            cursor_y = cursor_y + 50
                        self.one_info((cursor_y - 180) / 50)
                    elif (event.key == K_LEFT) | (event.key == K_q):
                        break
            else:
                pygame.display.update()
                continue
            break

    def one_info(self, i:int):
        font2 = pygame.font.Font("ipaexg.ttf", 20)
        pygame.draw.rect(self.screen, (0, 0, 0), (860, 50, 300, 700))
        pygame.draw.rect(self.screen, (0, 0, 0), (1190, 50, 200, 200))
        text_name = font2.render("NAME: " + str(self.member.member[i].get_name()), True, (255, 255, 255))
        text_level = font2.render("LEVEL: " + str(self.member.member[i].get_level()), True, (255, 255, 255))
        text_hp = font2.render("HP: " + str(self.member.member[i].get_hp()), True, (255, 255, 255))
        text_mp = font2.render("MP: " + str(self.member.member[i].get_mp()), True, (255, 255, 255))
        text_attack = font2.render("ATTACK: " + str(self.member.member[i].get_attack()), True, (255, 255, 255))
        text_difence = font2.render("DIFENCE: " + str(self.member.member[i].get_difence()), True, (255, 255, 255))
        text_mattack = font2.render("MAGIC ATTACK: " + str(self.member.member[i].get_magic_attack()), True, (255, 255, 255))
        text_mdifence = font2.render("MAGIC DIFENCE: " + str(self.member.member[i].get_magic_difence()), True, (255, 255, 255))
        text_speed = font2.render("SPEED: " + str(self.member.member[i].get_speed()), True, (255, 255, 255))
        text_experiment = font2.render("Experiment: " + str(self.member.member[i].get_experiment()), True, (255, 255, 255))
        text_next_experiment = font2.render("next: " + str(self.member.member[i].get_next_experiment()), True, (255, 255, 255))

        self.screen.blit(text_name, (880, 100))
        self.screen.blit(text_level, (880, 150))
        self.screen.blit(text_hp, (880, 200))
        self.screen.blit(text_mp, (880, 250))
        self.screen.blit(text_attack, (880, 300))
        self.screen.blit(text_difence, (880, 350))
        self.screen.blit(text_mattack, (880, 400))
        self.screen.blit(text_mdifence, (880, 450))
        self.screen.blit(text_speed, (880, 500))
        self.screen.blit(text_experiment, (880, 550))
        self.screen.blit(text_next_experiment, (880, 600))
        self.member.member[i].draw_image(self.screen, 1290, 150)


    def item_menu(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (300, 210, 400, 400))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if (event.key == K_LEFT) | (event.key == K_q):
                        break
            else:
                pygame.display.update()
                continue
            break

    def any_menu(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (300, 310, 400, 400))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if (event.key == K_LEFT) | (event.key == K_q):
                        break
            else:
                pygame.display.update()
                continue
            break

    def save_menu(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (300, 410, 200, 100))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if (event.key == K_LEFT) | (event.key == K_q):
                        break
            else:
                pygame.display.update()
                continue
            break
