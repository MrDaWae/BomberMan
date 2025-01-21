#déplacement, origine en bas à gauche,13 horizontal , 11 vertical
from pygame.locals import *
import pygame
import sys
import random
pygame.init()
game_running = True
display = pygame.display.set_mode((100,100))
class Bomberman:
    def __init__(self):
        self.terrain=[['c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','o','o','o','o','o','o','o','o','o','o','o','o','o','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','o','o','o','o','o','o','o','o','o','o','o','o','o','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','o','o','o','o','o','o','o','o','o','o','o','o','o','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','o','o','o','o','o','o','o','o','o','o','o','o','o','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','o','o','o','o','o','o','o','o','o','o','o','o','o','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','o','o','o','o','o','o','o','o','o','o','o','o','o','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','o','o','o','o','o','o','o','o','o','o','o','o','o','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','o','o','o','o','o','o','o','o','o','o','o','o','o','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','o','o','o','o','o','o','o','o','o','o','o','o','o','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','o','o','o','o','o','o','o','o','o','o','o','o','o','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','o','o','o','o','o','o','o','o','o','o','o','o','o','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c']]

        self.x=6
        self.y=6
        self.active=0
        self.bonus=0
        self.score=0
        self.temp=0
    def stageactive(self):
        self.active=1
        for i in range(6,len(self.terrain)-6):
            print (self.terrain[i][6:19])
        print("")
    def initialisation(self):
        self.terrain[6][6]="p"
        print(self.score)
        self.stageactive()
    def droite(self):
        if self.x<18:
            if self.terrain[self.y][self.x]=="P+B":
                self.terrain[self.y][self.x]="b"
                self.x+=1
            else:
                self.terrain[self.y][self.x]="o"
                self.x+=1
            if self.x>18:
                self.x=18
            if self.terrain[self.y][self.x]=="+":
                game.evolution_bombe()
            if self.terrain[self.y][self.x]=="A":
                game.score_fruit(0)
            if self.terrain[self.y][self.x]=="O":
                game.score_fruit(1)
            if self.terrain[self.y][self.x]=="P":
                game.score_fruit(2)
            if self.terrain[self.y][self.x]=="R":
                game.score_fruit(3)
            if self.terrain[self.y][self.x]=="T":
                game.score_fruit(4)
            if self.terrain[self.y][self.x]=="M":
                game.score_fruit(5)
            if self.terrain[self.y][self.x]=="J":
                game.score_fruit(6)
            if self.terrain[self.y][self.x]=="I":
                game.score_fruit(7)
            if self.terrain[self.y][self.x]=="D":
                game.gameover()
            if self.terrain[self.y][self.x]=="e":
                game.gameover()
            if self.terrain[self.y][self.x]=="b":
                self.terrain[self.y][self.x]="P+B"
            else:
                self.terrain[self.y][self.x]="p"
                print(self.score)
            game.stageactive()
    def gauche(self):
        if self.x>6:
            if self.terrain[self.y][self.x]=="P+B":
                self.terrain[self.y][self.x]="b"
                self.x-=1
            else:
                self.terrain[self.y][self.x]="o"
                self.x-=1
            if self.x<6:
                self.x=6
            if self.terrain[self.y][self.x]=="+":
                game.evolution_bombe()
            if self.terrain[self.y][self.x]=="A":
                game.score_fruit(0)
            if self.terrain[self.y][self.x]=="O":
                game.score_fruit(1)
            if self.terrain[self.y][self.x]=="P":
                game.score_fruit(2)
            if self.terrain[self.y][self.x]=="R":
                game.score_fruit(3)
            if self.terrain[self.y][self.x]=="T":
                game.score_fruit(4)
            if self.terrain[self.y][self.x]=="M":
                game.score_fruit(5)
            if self.terrain[self.y][self.x]=="J":
                game.score_fruit(6)
            if self.terrain[self.y][self.x]=="I":
                game.score_fruit(7)
            if self.terrain[self.y][self.x]=="D":
                game.gameover()
            if self.terrain[self.y][self.x]=="e":
                game.gameover()
            if self.terrain[self.y][self.x]=="b":
                self.terrain[self.y][self.x]="P+B"
            else:
                self.terrain[self.y][self.x]="p"
                print(self.score)
            game.stageactive()
    def haut(self):
        if self.y>6:
            if self.terrain[self.y][self.x]=="P+B":
                self.terrain[self.y][self.x]="b"
                self.y-=1
            else:
                self.terrain[self.y][self.x]="o"
                self.y-=1
            if self.y<6:
                self.y=6
            if self.terrain[self.y][self.x]=="+":
                game.evolution_bombe()
            if self.terrain[self.y][self.x]=="A":
                game.score_fruit(0)
            if self.terrain[self.y][self.x]=="O":
                game.score_fruit(1)
            if self.terrain[self.y][self.x]=="P":
                game.score_fruit(2)
            if self.terrain[self.y][self.x]=="R":
                game.score_fruit(3)
            if self.terrain[self.y][self.x]=="T":
                game.score_fruit(4)
            if self.terrain[self.y][self.x]=="M":
                game.score_fruit(5)
            if self.terrain[self.y][self.x]=="J":
                game.score_fruit(6)
            if self.terrain[self.y][self.x]=="I":
                game.score_fruit(7)
            if self.terrain[self.y][self.x]=="D":
                game.gameover()
            if self.terrain[self.y][self.x]=="e":
                game.gameover()
            if self.terrain[self.y][self.x]=="b":
                self.terrain[self.y][self.x]="P+B"
            else:
                self.terrain[self.y][self.x]="p"
                print(self.score)
            game.stageactive()
    def bas(self):
        if self.y<16:
            if self.terrain[self.y][self.x]=="P+B":
                self.terrain[self.y][self.x]="b"
                self.y+=1
            else:
                self.terrain[self.y][self.x]="o"
                self.y+=1
            if self.terrain[self.y][self.x]=="+":
                game.evolution_bombe()
            if self.terrain[self.y][self.x]=="A":
                game.score_fruit(0)
            if self.terrain[self.y][self.x]=="O":
                game.score_fruit(1)
            if self.terrain[self.y][self.x]=="P":
                game.score_fruit(2)
            if self.terrain[self.y][self.x]=="R":
                game.score_fruit(3)
            if self.terrain[self.y][self.x]=="T":
                game.score_fruit(4)
            if self.terrain[self.y][self.x]=="M":
                game.score_fruit(5)
            if self.terrain[self.y][self.x]=="J":
                game.score_fruit(6)
            if self.terrain[self.y][self.x]=="I":
                game.score_fruit(7)
            if self.terrain[self.y][self.x]=="D":
                game.gameover()
            if self.terrain[self.y][self.x]=="e":
                game.gameover()
            if self.terrain[self.y][self.x]=="b":
                self.terrain[self.y][self.x]="P+B"
            else:
                self.terrain[self.y][self.x]="p"
                print(self.score)
            game.stageactive()
    def evolution_bombe(self):
        self.temp=self.temp+1
        if self.temp == 1:
            self.bonus = self.bonus+1
            game.bombe()
            game.score_arcade()
        if self.temp == 2:
            self.bonus = self.bonus+1
            game.bombe()
            game.score_arcade()
        if self.temp == 3:
            self.bonus = self.bonus+1
            game.bombe()
            game.score_arcade()
        if self.temp == 4:
            self.bonus = self.bonus+1
            game.bombe()
            game.score_arcade()
        if self.temp == 5:
            self.bonus = self.bonus+1
            game.bombe()
            game.score_arcade()
    def score_arcade(self):
        if self.bonus == 1:
            self.score=self.score+50
        if self.bonus == 2:
            self.score=self.score+100
        if self.bonus == 3:
            self.score=self.score+200
        if self.bonus == 4:
            self.score = self.score+500
        if self.bonus == 5:
            self.score = self.score+1000
    def score_fruit(self,fruit):
        #0=Apple,1=Orange,2=Pineapple,3=riceball,4=takoyaki,5=meat,6=jelly,7=ice_cream
        if fruit==0:
            self.score=self.score+10
        if fruit==1:
            self.score=self.score+20
        if fruit==2:
            self.score=self.score+50
        if fruit==3:
            self.score=self.score+100
        if fruit==4:
            self.score=self.score+200
        if fruit==5:
            self.score=self.score+500
        if fruit==6:
            self.score=self.score+750
        if fruit==7:
            self.score=self.score+1000
    def bombe(self):
        if self.bonus == 0 :
            return 0
        if self.bonus == 1 :
            return 1
        if self.bonus == 2 :
            return 2
        if self.bonus == 3 :
            return 3
        if self.bonus == 4 :
            return 4
        if self.bonus == 5 :
            return 5
    def placer4Ennemi(self):
        for i in range(0,4):
            yennemi=random.randint(6,16)
            xennemi=random.randint(6,18)
            while self.terrain[yennemi][xennemi]!='o':
                yennemi=random.randint(6,16)
                xennemi=random.randint(6,18)
            self.terrain[yennemi][xennemi]='D'
            self.stageactive()
    def bonus_spawn(self):
        for i in range(0,5):
            yscore=random.randint(6,16)
            xscore=random.randint(6,18)
            while self.terrain[yscore][xscore]!='o':
                yscore=random.randint(6,16)
                xscore=random.randint(6,18)
            self.terrain[yscore][xscore]='+'
            self.stageactive()
    def fruits(self):
        #Apple,Pineapple,Orange,riceball,meat,jelly,ice cream,takoyaki
        liste=["A","P","O","R","M","J","I","T"]
        for i in range(len(liste)):
            yscore=random.randint(6,16)
            xscore=random.randint(6,18)
            while self.terrain[yscore][xscore]!='o':
                yscore=random.randint(6,16)
                xscore=random.randint(6,18)
            self.terrain[yscore][xscore]=liste[i]
            self.stageactive()
    def Game(self):
        game_running=True
        bombe_restriction=0
        evt=pygame.USEREVENT+1
        evt_temp=pygame.USEREVENT+2
        while game_running:
            bombe_lvl=game.bombe()
            if self.terrain[self.y][self.x]=="e":
                game.gameover()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        game.gauche()
                    if event.key == pygame.K_w:
                        game.haut()
                    if event.key == pygame.K_d:
                        game.droite()
                    if event.key == pygame.K_s:
                        game.bas()
                    if event.key == pygame.K_n:
                        pygame.quit()
                    if event.key == pygame.K_f:
                        print(self.score)
                        if bombe_restriction == 0:
                            pygame.time.set_timer(evt,2000)
                            y=self.y
                            x=self.x
                            self.terrain[y][x]='P+B'
                            self.stageactive()
                            bombe_restriction=1
                if event.type==evt and bombe_lvl ==0:
                    print(self.score)
                    self.terrain[y][x]='e'
                    self.terrain[y+1][x]='e'
                    self.terrain[y-1][x]='e'
                    self.terrain[y][x+1]='e'
                    self.terrain[y][x-1]='e'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,1000)
                    pygame.time.set_timer(evt,0)
                if event.type==evt and bombe_lvl ==1:
                    print(self.score)
                    self.terrain[y][x]='e'
                    self.terrain[y+1][x]='e'
                    self.terrain[y-1][x]='e'
                    self.terrain[y][x+1]='e'
                    self.terrain[y][x-1]='e'
                    self.terrain[y+2][x]='e'
                    self.terrain[y-2][x]='e'
                    self.terrain[y][x+2]='e'
                    self.terrain[y][x-2]='e'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,1000)
                    pygame.time.set_timer(evt,0)
                if event.type==evt and bombe_lvl ==2:
                    print(self.score)
                    self.terrain[y][x]='e'
                    self.terrain[y+1][x]='e'
                    self.terrain[y-1][x]='e'
                    self.terrain[y][x+1]='e'
                    self.terrain[y][x-1]='e'
                    self.terrain[y+2][x]='e'
                    self.terrain[y-2][x]='e'
                    self.terrain[y][x+2]='e'
                    self.terrain[y][x-2]='e'
                    self.terrain[y+3][x]='e'
                    self.terrain[y-3][x]='e'
                    self.terrain[y][x+3]='e'
                    self.terrain[y][x-3]='e'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,1000)
                    pygame.time.set_timer(evt,0)
                if event.type==evt and bombe_lvl ==3:
                    print(self.score)
                    self.terrain[y][x]='e'
                    self.terrain[y+1][x]='e'
                    self.terrain[y-1][x]='e'
                    self.terrain[y][x+1]='e'
                    self.terrain[y][x-1]='e'
                    self.terrain[y+2][x]='e'
                    self.terrain[y-2][x]='e'
                    self.terrain[y][x+2]='e'
                    self.terrain[y][x-2]='e'
                    self.terrain[y+3][x]='e'
                    self.terrain[y-3][x]='e'
                    self.terrain[y][x+3]='e'
                    self.terrain[y][x-3]='e'
                    self.terrain[y+4][x]='e'
                    self.terrain[y-4][x]='e'
                    self.terrain[y][x+4]='e'
                    self.terrain[y][x-4]='e'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,1000)
                    pygame.time.set_timer(evt,0)
                if event.type==evt and bombe_lvl ==4:
                    print(self.score)
                    self.terrain[y][x]='e'
                    self.terrain[y+1][x]='e'
                    self.terrain[y-1][x]='e'
                    self.terrain[y][x+1]='e'
                    self.terrain[y][x-1]='e'
                    self.terrain[y+2][x]='e'
                    self.terrain[y-2][x]='e'
                    self.terrain[y][x+2]='e'
                    self.terrain[y][x-2]='e'
                    self.terrain[y+3][x]='e'
                    self.terrain[y-3][x]='e'
                    self.terrain[y][x+3]='e'
                    self.terrain[y][x-3]='e'
                    self.terrain[y+4][x]='e'
                    self.terrain[y-4][x]='e'
                    self.terrain[y][x+4]='e'
                    self.terrain[y][x-4]='e'
                    self.terrain[y+5][x]='e'
                    self.terrain[y-5][x]='e'
                    self.terrain[y][x+5]='e'
                    self.terrain[y][x-5]='e'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,1000)
                    pygame.time.set_timer(evt,0)
                if event.type==evt and bombe_lvl ==5:
                    print(self.score)
                    self.terrain[y][x]='e'
                    self.terrain[y+1][x]='e'
                    self.terrain[y-1][x]='e'
                    self.terrain[y][x+1]='e'
                    self.terrain[y][x-1]='e'
                    self.terrain[y+2][x]='e'
                    self.terrain[y-2][x]='e'
                    self.terrain[y][x+2]='e'
                    self.terrain[y][x-2]='e'
                    self.terrain[y+3][x]='e'
                    self.terrain[y-3][x]='e'
                    self.terrain[y][x+3]='e'
                    self.terrain[y][x-3]='e'
                    self.terrain[y+4][x]='e'
                    self.terrain[y-4][x]='e'
                    self.terrain[y][x+4]='e'
                    self.terrain[y][x-4]='e'
                    self.terrain[y+5][x]='e'
                    self.terrain[y-5][x]='e'
                    self.terrain[y][x+5]='e'
                    self.terrain[y][x-5]='e'
                    self.terrain[y+6][x]='e'
                    self.terrain[y-6][x]='e'
                    self.terrain[y][x+6]='e'
                    self.terrain[y][x-6]='e'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,1000)
                    pygame.time.set_timer(evt,0)
                if event.type==evt_temp  and bombe_lvl ==0:
                    print(self.score)
                    self.terrain[y][x]='o'
                    self.terrain[y+1][x]='o'
                    self.terrain[y-1][x]='o'
                    self.terrain[y][x+1]='o'
                    self.terrain[y][x-1]='o'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,0)
                    bombe_restriction=0
                if event.type==evt_temp  and bombe_lvl ==1:
                    print(self.score)
                    self.terrain[y][x]='o'
                    self.terrain[y+1][x]='o'
                    self.terrain[y-1][x]='o'
                    self.terrain[y][x+1]='o'
                    self.terrain[y][x-1]='o'
                    self.terrain[y+2][x]='o'
                    self.terrain[y-2][x]='o'
                    self.terrain[y][x+2]='o'
                    self.terrain[y][x-2]='o'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,0)
                    bombe_restriction=0
                if event.type==evt_temp  and bombe_lvl ==2:
                    print(self.score)
                    self.terrain[y][x]='o'
                    self.terrain[y+1][x]='o'
                    self.terrain[y-1][x]='o'
                    self.terrain[y][x+1]='o'
                    self.terrain[y][x-1]='o'
                    self.terrain[y+2][x]='o'
                    self.terrain[y-2][x]='o'
                    self.terrain[y][x+2]='o'
                    self.terrain[y][x-2]='o'
                    self.terrain[y+3][x]='o'
                    self.terrain[y-3][x]='o'
                    self.terrain[y][x+3]='o'
                    self.terrain[y][x-3]='o'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,0)
                    bombe_restriction=0
                if event.type==evt_temp  and bombe_lvl ==3:
                    print(self.score)
                    self.terrain[y][x]='o'
                    self.terrain[y+1][x]='o'
                    self.terrain[y-1][x]='o'
                    self.terrain[y][x+1]='o'
                    self.terrain[y][x-1]='o'
                    self.terrain[y+2][x]='o'
                    self.terrain[y-2][x]='o'
                    self.terrain[y][x+2]='o'
                    self.terrain[y][x-2]='o'
                    self.terrain[y+3][x]='o'
                    self.terrain[y-3][x]='o'
                    self.terrain[y][x+3]='o'
                    self.terrain[y][x-3]='o'
                    self.terrain[y+4][x]='o'
                    self.terrain[y-4][x]='o'
                    self.terrain[y][x+4]='o'
                    self.terrain[y][x-4]='o'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,0)
                    bombe_restriction=0
                if event.type==evt_temp  and bombe_lvl ==4:
                    print(self.score)
                    self.terrain[y][x]='o'
                    self.terrain[y+1][x]='o'
                    self.terrain[y-1][x]='o'
                    self.terrain[y][x+1]='o'
                    self.terrain[y][x-1]='o'
                    self.terrain[y+2][x]='o'
                    self.terrain[y-2][x]='o'
                    self.terrain[y][x+2]='o'
                    self.terrain[y][x-2]='o'
                    self.terrain[y+3][x]='o'
                    self.terrain[y-3][x]='o'
                    self.terrain[y][x+3]='o'
                    self.terrain[y][x-3]='o'
                    self.terrain[y+4][x]='o'
                    self.terrain[y-4][x]='o'
                    self.terrain[y][x+4]='o'
                    self.terrain[y][x-4]='o'
                    self.terrain[y+5][x]='o'
                    self.terrain[y-5][x]='o'
                    self.terrain[y][x+5]='o'
                    self.terrain[y][x-5]='o'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,0)
                    bombe_restriction=0
                if event.type==evt_temp  and bombe_lvl ==5:
                    print(self.score)
                    self.terrain[y][x]='o'
                    self.terrain[y+1][x]='o'
                    self.terrain[y-1][x]='o'
                    self.terrain[y][x+1]='o'
                    self.terrain[y][x-1]='o'
                    self.terrain[y+2][x]='o'
                    self.terrain[y-2][x]='o'
                    self.terrain[y][x+2]='o'
                    self.terrain[y][x-2]='o'
                    self.terrain[y+3][x]='o'
                    self.terrain[y-3][x]='o'
                    self.terrain[y][x+3]='o'
                    self.terrain[y][x-3]='o'
                    self.terrain[y+4][x]='o'
                    self.terrain[y-4][x]='o'
                    self.terrain[y][x+4]='o'
                    self.terrain[y][x-4]='o'
                    self.terrain[y+5][x]='o'
                    self.terrain[y-5][x]='o'
                    self.terrain[y][x+5]='o'
                    self.terrain[y][x-5]='o'
                    self.terrain[y+6][x]='o'
                    self.terrain[y-6][x]='o'
                    self.terrain[y][x+6]='o'
                    self.terrain[y][x-6]='o'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,0)
                    bombe_restriction=0
game=Bomberman()
game.stageactive()
game.bonus_spawn()
game.placer4Ennemi()
game.fruits()
game.initialisation()
game.Game()

pygame.quit()







