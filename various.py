from pygame.locals import *
import pygame
import sys
from game.object.player_object.player import Player

def main():
    pygame.init()    # Pygameを初期化
    screen = pygame.display.set_mode((0, 0))    # 画面を作成
    pygame.display.set_caption("S.C.MAGI")    # タイトルを作成


    #テキストの設定については前回の記事をご覧ください。
    
    running = True

    #メインループ
    while running:
        screen.fill((153,255,50))

        me = Player(screen)
        screen.blit(me.get_surface(), me.get_dest())
       
        # 図形を描画
        #---------------  ここからが今回の追加部分  --------------------------
        
        pygame.draw.rect(screen, (0,101,50), (20,70,10,180))
        pygame.draw.rect(screen, (255,0,0), (370,70,10,180))

        for i in range(50):
            k = i * 20 - 60
            pygame.draw.polygon(screen, (255,0,0), [[40 + k, 10], [50+k, 10],[20+k,60],[10+k, 60]])
            pygame.draw.polygon(screen, (255,0,0), [[40 + k, 270], [50+k, 270],[20+k,320],[10+k, 320]])

        #---------------  ここまで  --------------------------

        pygame.display.update() #描画処理を実行
        
        me.move()
                
if __name__=="__main__":
    main()