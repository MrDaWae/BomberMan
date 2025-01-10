#déplacement, origine en bas à gauche,13 horizontal , 11 vertical
from pygame.locals import *
import pygame
import sys
pygame.init()
game_running = True
display = pygame.display.set_mode((100,100))
class Bomberman:
    def __init__(self):
        self.terrain=[['o','o','o','o','o','o','o','o','o','o','o','o','o'],
                      ['o','o','o','o','o','o','o','o','o','o','o','o','o'],
                      ['o','o','o','o','o','o','o','o','o','o','o','o','o'],
                      ['o','o','o','o','o','o','o','o','o','o','o','o','o'],
                      ['o','o','o','o','o','o','o','o','o','o','o','o','o'],
                      ['o','o','o','o','o','o','o','o','o','o','o','o','o'],
                      ['o','o','o','o','o','o','o','o','o','o','o','o','o'],
                      ['o','o','o','o','o','o','o','o','o','o','o','o','o'],
                      ['o','o','o','o','o','o','o','o','o','o','o','o','o'],
                      ['o','o','o','o','o','o','o','o','o','o','o','o','o'],
                      ['o','o','o','o','o','o','o','o','o','o','o','o','o']]
        self.x=0
        self.y=0
        self.active=0
    def stageactive(self):
        self.active=1
        for i in range (len(self.terrain)):
            print(self.terrain[i])
        print("")
    def initialisation(self):
        self.terrain[0][0]="p"
        self.stageactive()
    def droite(self):
        if self.x<12:
            if self.terrain[self.y][self.x]=="P+B":
                self.terrain[self.y][self.x]="b"
                self.x+=1
            else:
                self.terrain[self.y][self.x]="o"
                self.x+=1
            if self.x>12:
                self.x=12
            if self.terrain[self.y][self.x]=="b":
                self.terrain[self.y][self.x]="P+B"
            else:
                self.terrain[self.y][self.x]="p"
            game.stageactive()
    def gauche(self):
        if self.x>0:
            if self.terrain[self.y][self.x]=="P+B":
                self.terrain[self.y][self.x]="b"
                self.x-=1
            else:
                self.terrain[self.y][self.x]="o"
                self.x-=1
            if self.x<0:
                self.x=0
            if self.terrain[self.y][self.x]=="b":
                self.terrain[self.y][self.x]="P+B"
            else:
                self.terrain[self.y][self.x]="p"
            game.stageactive()
    def haut(self):
        if self.y>0:
            if self.terrain[self.y][self.x]=="P+B":
                self.terrain[self.y][self.x]="b"
                self.y-=1
            else:
                self.terrain[self.y][self.x]="o"
                self.y-=1
            if self.y<0:
                self.y=0
            if self.terrain[self.y][self.x]=="b":
                self.terrain[self.y][self.x]="P+B"
            else:
                self.terrain[self.y][self.x]="p"
            game.stageactive()
    def bas(self):
         if self.y<10:
            if self.terrain[self.y][self.x]=="P+B":
                self.terrain[self.y][self.x]="b"
                self.y+=1
            else:
                self.terrain[self.y][self.x]="o"
                self.y+=1
            if self.y>10:
                self.y=10
            if self.terrain[self.y][self.x]=="b":
                self.terrain[self.y][self.x]="P+B"
            else:
                self.terrain[self.y][self.x]="p"
            game.stageactive()
    def Game(self):
        game_running=True
        bombe_restriction=0
        evt=pygame.USEREVENT+1
        evt_temp=pygame.USEREVENT+2
        while game_running:
            if self.terrain[self.y][self.x]=="e":
                game.gameover()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print("Key Q has been pressed")
                        game.gauche()
                    if event.key == pygame.K_w:
                        print("Key Z has been pressed")
                        game.haut()
                    if event.key == pygame.K_d:
                        #print("Key D has been pressed")
                        game.droite()
                    if event.key == pygame.K_s:
                        print("Key S has been pressed")
                        game.bas()
                    if event.key == pygame.K_n:
                        pygame.quit()
                    if event.key == pygame.K_f:
                        if bombe_restriction == 0:
                            print("key f has been pressed")
                            pygame.time.set_timer(evt,2000)
                            y=self.y
                            x=self.x
                            self.terrain[y][x]='P+B'
                            print("")
                            self.stageactive()
                            bombe_restriction=1
                if event.type==evt:
                    if y==10 and x==0:
                        self.terrain[y][x]='e'
                        self.terrain[y-1][x]='e'
                        self.terrain[y][x+1]='e'
                    elif y==0 and x==0:
                        self.terrain[y][x]='e'
                        self.terrain[y+1][x]='e'
                        self.terrain[y][x+1]='e'
                    elif y==10 and x==12:
                        self.terrain[y][x]='e'
                        self.terrain[y-1][x]='e'
                        self.terrain[y][x-1]='e'
                    elif y==0 and x==12:
                        self.terrain[y][x]='e'
                        self.terrain[y+1][x]='e'
                        self.terrain[y][x-1]='e'
                    elif y==0:
                        self.terrain[y][x]='e'
                        self.terrain[y+1][x]='e'
                        self.terrain[y][x+1]='e'
                        self.terrain[y][x-1]='e'
                    elif y==10:
                        self.terrain[y][x]='e'
                        self.terrain[y-1][x]='e'
                        self.terrain[y][x+1]='e'
                        self.terrain[y][x-1]='e'
                    elif x==12:
                        self.terrain[y][x]='e'
                        self.terrain[y-1][x]='e'
                        self.terrain[y][x+1]='e'
                        self.terrain[y][x-1]='e'
                    elif x==0:
                        self.terrain[y][x]='e'
                        self.terrain[y+1][x]='e'
                        self.terrain[y][x+1]='e'
                        self.terrain[y][x-1]='e'
                    else:
                        self.terrain[y][x]='e'
                        self.terrain[y+1][x]='e'
                        self.terrain[y-1][x]='e'
                        self.terrain[y][x+1]='e'
                        self.terrain[y][x-1]='e'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,1000)
                    pygame.time.set_timer(evt,0)
                if event.type==evt_temp:
                    if y==10 and x==0:
                        self.terrain[y][x]='o'
                        self.terrain[y-1][x]='o'
                        self.terrain[y][x+1]='o'
                    elif y==0 and x==0:
                        self.terrain[y][x]='o'
                        self.terrain[y+1][x]='o'
                        self.terrain[y][x+1]='o'
                    elif y==10 and x==12:
                        self.terrain[y][x]='o'
                        self.terrain[y-1][x]='o'
                        self.terrain[y][x-1]='o'
                    elif y==0 and x==12:
                        self.terrain[y][x]='o'
                        self.terrain[y+1][x]='o'
                        self.terrain[y][x-1]='o'
                    elif y==0:
                        self.terrain[y][x]='o'
                        self.terrain[y+1][x]='o'
                        self.terrain[y][x+1]='o'
                        self.terrain[y][x-1]='o'
                    elif y==10:
                        self.terrain[y][x]='o'
                        self.terrain[y-1][x]='o'
                        self.terrain[y][x+1]='o'
                        self.terrain[y][x-1]='o'
                    elif x==12:
                        self.terrain[y][x]='o'
                        self.terrain[y-1][x]='o'
                        self.terrain[y][x+1]='o'
                        self.terrain[y][x-1]='o'
                    elif x==0:
                        self.terrain[y][x]='o'
                        self.terrain[y+1][x]='o'
                        self.terrain[y][x+1]='o'
                        self.terrain[y][x-1]='o'
                    else:
                        self.terrain[y][x]='o'
                        self.terrain[y+1][x]='o'
                        self.terrain[y-1][x]='o'
                        self.terrain[y][x+1]='o'
                        self.terrain[y][x-1]='o'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,0)
                    bombe_restriction=0
game=Bomberman()
print(game.stageactive())
game.initialisation()
game.Game()
pygame.quit()







