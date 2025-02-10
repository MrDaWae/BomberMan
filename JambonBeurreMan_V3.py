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
                      ['c','c','c','c','c','c','.','.','.','.','.','.','.','.','.','.','.','.','.','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','.','.','.','.','.','.','.','.','.','.','.','.','.','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','.','.','.','.','.','.','.','.','.','.','.','.','.','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','.','.','.','.','.','.','.','.','.','.','.','.','.','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','.','.','.','.','.','.','.','.','.','.','.','.','.','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','.','.','.','.','.','.','.','.','.','.','.','.','.','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','.','.','.','.','.','.','.','.','.','.','.','.','.','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','.','.','.','.','.','.','.','.','.','.','.','.','.','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','.','.','.','.','.','.','.','.','.','.','.','.','.','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','.','.','.','.','.','.','.','.','.','.','.','.','.','c','c','c','c','c','c'],
                      ['c','c','c','c','c','c','.','.','.','.','.','.','.','.','.','.','.','.','.','c','c','c','c','c','c'],
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
        self.tirage=0
        self.xennemi1=0
        self.yennemi1=0
        self.temporaliter_s=0
        self.temporaliter_m=0

    def stageactive(self):
        self.active=1
        for i in range(6,len(game.terrain)-6):
            print (game.terrain[i][6:19])
        print("")

    def initialisation(self):
        self.terrain[self.y][self.x]="p"
        print(self.score)
        self.stageactive()

    def droite(self):
        if self.x<18:
            if self.terrain[self.y][self.x]=="P+B":
                self.terrain[self.y][self.x]="b"
                self.x+=1
            else:
                self.terrain[self.y][self.x]="."
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
                game.timer()
                print(self.score)
            game.stageactive()

    def gauche(self):
        if self.x>6:
            if self.terrain[self.y][self.x]=="P+B":
                self.terrain[self.y][self.x]="b"
                self.x-=1
            else:
                self.terrain[self.y][self.x]="."
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
                game.timer()
                print(self.score)
            game.stageactive()

    def haut(self):
        if self.y>6:
            if self.terrain[self.y][self.x]=="P+B":
                self.terrain[self.y][self.x]="b"
                self.y-=1
            else:
                self.terrain[self.y][self.x]="."
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
                game.timer()
                print(self.score)
            game.stageactive()

    def bas(self):
        if self.y<16:
            if self.terrain[self.y][self.x]=="P+B":
                self.terrain[self.y][self.x]="b"
                self.y+=1
            else:
                self.terrain[self.y][self.x]="."
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
                game.timer()
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

    def Ennemi_comportement1(self):
        #tue l'ennemi et son cadavre
        if self.terrain[self.yennemi1][self.xennemi1]=="e":
            self.tirage=0
            self.terrain[self.yennemi1][self.xennemi1]='.'
        #l'ennemi se deplace
        if self.tirage == 1:
                #l'ennemi est con
                action=random.randint(1,4)
                if action==1:
                    # en bas
                    self.terrain[self.yennemi1][self.xennemi1]='.'
                    self.yennemi1=self.yennemi1+1
                    if self.yennemi1>16 :
                                self.yennemi1=16
                    if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                        self.yennemi1=self.yennemi1-1
                        deplacementRandom=random.randint(1,2)
                        self.terrain[self.yennemi1][self.xennemi1]='.'

                        if deplacementRandom==1:
                            self.xennemi1=self.xennemi1+1
                            if self.xennemi1>18:
                                    self.xennemi1=18
                            self.terrain[self.yennemi1][self.xennemi1]='D'
                        else:
                            self.xennemi1=self.xennemi1-1
                            if self.xennemi1<6:
                                self.xennemi1=6
                            self.terrain[self.yennemi1][self.xennemi1]='D'

                if action==2:
                    # a droite
                    self.terrain[self.yennemi1][self.xennemi1]='.'
                    self.xennemi1=self.xennemi1+1
                    if self.xennemi1>18:
                                    self.xennemi1=18
                    if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                        self.xennemi1=self.xennemi1-1
                        deplacementRandom=random.randint(1,2)
                        self.terrain[self.yennemi1][self.xennemi1]='.'
                        if deplacementRandom==1:
                            self.yennemi1=self.yennemi1+1
                            if self.yennemi1>16 :
                                self.yennemi1=16
                            self.terrain[self.yennemi1][self.xennemi1]='D'

                        else:
                            self.yennemi1=self.yennemi1-1
                            if self.yennemi1<6:
                                self.yennemi1=6
                            self.terrain[self.yennemi1][self.xennemi1]='D'

                if action==3:
                    # en haut
                    self.terrain[self.yennemi1][self.xennemi1]='.'
                    self.yennemi1=self.yennemi1-1
                    if self.yennemi1<6:
                                self.yennemi1=6
                    if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                        self.yennemi1=self.yennemi1+1
                        deplacementRandom=random.randint(1,2)
                        self.terrain[self.yennemi1][self.xennemi1]='.'
                        if deplacementRandom==1:
                            self.xennemi1=self.xennemi1+1
                            if self.xennemi1>18:
                                    self.xennemi1=18
                            self.terrain[self.yennemi1][self.xennemi1]='D'

                        else:
                            self.xennemi1=self.xennemi1-1
                            if self.xennemi1<6:
                                self.xennemi1=6
                            self.terrain[self.yennemi1][self.xennemi1]='D'

                if action==4:
                    # a gauche
                    self.terrain[self.yennemi1][self.xennemi1]='.'
                    self.xennemi1=self.xennemi1-1
                    if self.xennemi1<6:
                                self.xennemi1=6
                    if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                        self.xennemi1=self.xennemi1+1
                        deplacementRandom=random.randint(1,2)
                        self.terrain[self.yennemi1][self.xennemi1]='.'
                        if deplacementRandom==1:
                            self.yennemi1=self.yennemi1+1
                            if self.yennemi1>16 :
                                self.yennemi1=16
                            self.terrain[self.yennemi1][self.xennemi1]='D'

                        else:
                            self.yennemi1=self.yennemi1-1
                            if self.yennemi1<6:
                                self.yennemi1=6
                            self.terrain[self.yennemi1][self.xennemi1]='D'

        if self.tirage == 2:
                #l'ennemi est chercheur
                if (self.yennemi1!=self.y or self.xennemi1!=self.x) :
                    action=random.randint(1,2)

                    if self.yennemi1==self.y:
                        diff=(self.x)-(self.xennemi1)

                        if diff<0:
                            # a gauche
                            self.terrain[self.yennemi1][self.xennemi1]='.'
                            self.xennemi1=self.xennemi1-1
                            if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                self.xennemi1=self.xennemi1+1
                                deplacementRandom=random.randint(1,2)
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                if deplacementRandom==1:
                                    self.yennemi1=self.yennemi1+1
                                    if self.yennemi1>16 :
                                        self.yennemi1=16
                                    self.terrain[self.yennemi1][self.xennemi1]='D'

                                else:
                                    self.yennemi1=self.yennemi1-1
                                    if self.yennemi1<6:
                                        self.yennemi1=6
                                    self.terrain[self.yennemi1][self.xennemi1]='D'
                        elif diff>0:
                            # a droite
                            self.terrain[self.yennemi1][self.xennemi1]='.'
                            self.xennemi1=self.xennemi1+1
                            if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                self.xennemi1=self.xennemi1-1
                                deplacementRandom=random.randint(1,2)
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                if deplacementRandom==1:
                                    self.yennemi1=self.yennemi1+1
                                    if self.yennemi1>16 :
                                        self.yennemi1=16
                                    self.terrain[self.yennemi1][self.xennemi1]='D'

                                else:
                                    self.yennemi1=self.yennemi1-1
                                    if self.yennemi1<6:
                                        self.yennemi1=6
                                    self.terrain[self.yennemi1][self.xennemi1]='D'




                    elif self.xennemi1==self.x:
                        diff=(self.y)-(self.yennemi1)
                        if diff<0:
                            # en haut
                            self.terrain[self.yennemi1][self.xennemi1]='.'
                            self.yennemi1=self.yennemi1-1
                            if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                self.yennemi1=self.yennemi1+1
                                deplacementRandom=random.randint(1,2)
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                if deplacementRandom==1:
                                    self.xennemi1=self.xennemi1+1
                                    if self.xennemi1>18:
                                            self.xennemi1=18
                                    self.terrain[self.yennemi1][self.xennemi1]='D'

                                else:
                                    self.xennemi1=self.xennemi1-1
                                    if self.xennemi1<6:
                                        self.xennemi1=6
                                    self.terrain[self.yennemi1][self.xennemi1]='D'


                        elif diff>0:
                            # en bas
                            self.terrain[self.yennemi1][self.xennemi1]='.'
                            self.yennemi1=self.yennemi1+1
                            if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                self.yennemi1=self.yennemi1-1
                                deplacementRandom=random.randint(1,2)
                                self.terrain[self.yennemi1][self.xennemi1]='.'

                                if deplacementRandom==1:
                                    self.xennemi1=self.xennemi1+1
                                    if self.xennemi1>18:
                                            self.xennemi1=18
                                    self.terrain[self.yennemi1][self.xennemi1]='D'
                                else:
                                    self.xennemi1=self.xennemi1-1
                                    if self.xennemi1<6:
                                        self.xennemi1=6
                                    self.terrain[self.yennemi1][self.xennemi1]='D'



                    else:
                        if action==1:
                            diff=(self.x)-(self.xennemi1)
                            if diff<0:
                                # a gauche
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                self.xennemi1=self.xennemi1-1
                                if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                    self.xennemi1=self.xennemi1+1
                                    deplacementRandom=random.randint(1,2)
                                    self.terrain[self.yennemi1][self.xennemi1]='.'
                                    if deplacementRandom==1:
                                        self.yennemi1=self.yennemi1+1
                                        if self.yennemi1>16 :
                                            self.yennemi1=16
                                        self.terrain[self.yennemi1][self.xennemi1]='D'

                                    else:
                                        self.yennemi1=self.yennemi1-1
                                        if self.yennemi1<6:
                                            self.yennemi1=6
                                        self.terrain[self.yennemi1][self.xennemi1]='D'
                            elif diff>0:
                                # a droite
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                self.xennemi1=self.xennemi1+1
                                if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                    self.xennemi1=self.xennemi1-1
                                    deplacementRandom=random.randint(1,2)
                                    self.terrain[self.yennemi1][self.xennemi1]='.'
                                    if deplacementRandom==1:
                                        self.yennemi1=self.yennemi1+1
                                        if self.yennemi1>16 :
                                            self.yennemi1=16
                                        self.terrain[self.yennemi1][self.xennemi1]='D'

                                    else:
                                        self.yennemi1=self.yennemi1-1
                                        if self.yennemi1<6:
                                            self.yennemi1=6
                                        self.terrain[self.yennemi1][self.xennemi1]='D'


                        elif action==2:
                            diff=(self.y)-(self.yennemi1)
                            if diff<0:
                                 # en haut
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                self.yennemi1=self.yennemi1-1
                                if self.terrain[self.yennemi1][self.xennemi1]=='b' or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                    self.yennemi1=self.yennemi1+1
                                    deplacementRandom=random.randint(1,2)
                                    self.terrain[self.yennemi1][self.xennemi1]='.'

                                    if deplacementRandom==1:
                                        self.xennemi1=self.xennemi1+1
                                        if self.xennemi1>18:
                                                self.xennemi1=18
                                        self.terrain[self.yennemi1][self.xennemi1]='D'
                                    else:
                                        self.xennemi1=self.xennemi1-1
                                        if self.xennemi1<6:
                                            self.xennemi1=6
                                        self.terrain[self.yennemi1][self.xennemi1]='D'
                            elif diff>0:
                                 # en bas
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                self.yennemi1=self.yennemi1+1
                                if self.terrain[self.yennemi1][self.xennemi1]=='b' or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                    self.yennemi1=self.yennemi1-1
                                    deplacementRandom=random.randint(1,2)
                                    self.terrain[self.yennemi1][self.xennemi1]='.'

                                    if deplacementRandom==1:
                                        self.xennemi1=self.xennemi1+1
                                        if self.xennemi1>18:
                                                self.xennemi1=18
                                        self.terrain[self.yennemi1][self.xennemi1]='D'
                                    else:
                                        self.xennemi1=self.xennemi1-1
                                        if self.xennemi1<6:
                                            self.xennemi1=6
                                        self.terrain[self.yennemi1][self.xennemi1]='D'
        if self.tirage==3:
            action=random.randint(1,4)
            diffx=(self.x)-(self.xennemi1)
            diffy=(self.y)-(self.yennemi1)
            if diffx>=4 or diffy>=4 or diffx<=-4 or diffy<=-4:
                if action==1:
                    # en bas
                    self.terrain[self.yennemi1][self.xennemi1]='.'
                    self.yennemi1=self.yennemi1+1
                    if self.yennemi1>16 :
                                self.yennemi1=16
                    if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                        self.yennemi1=self.yennemi1-1
                        deplacementRandom=random.randint(1,2)
                        self.terrain[self.yennemi1][self.xennemi1]='.'

                        if deplacementRandom==1:
                            self.xennemi1=self.xennemi1+1
                            if self.xennemi1>18:
                                    self.xennemi1=18
                            self.terrain[self.yennemi1][self.xennemi1]='D'
                        else:
                            self.xennemi1=self.xennemi1-1
                            if self.xennemi1<6:
                                self.xennemi1=6
                            self.terrain[self.yennemi1][self.xennemi1]='D'

                if action==2:
                    # a droite
                    self.terrain[self.yennemi1][self.xennemi1]='.'
                    self.xennemi1=self.xennemi1+1
                    if self.xennemi1>18:
                                    self.xennemi1=18
                    if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                        self.xennemi1=self.xennemi1-1
                        deplacementRandom=random.randint(1,2)
                        self.terrain[self.yennemi1][self.xennemi1]='.'
                        if deplacementRandom==1:
                            self.yennemi1=self.yennemi1+1
                            if self.yennemi1>16 :
                                self.yennemi1=16
                            self.terrain[self.yennemi1][self.xennemi1]='D'

                        else:
                            self.yennemi1=self.yennemi1-1
                            if self.yennemi1<6:
                                self.yennemi1=6
                            self.terrain[self.yennemi1][self.xennemi1]='D'

                if action==3:
                    # en haut
                    self.terrain[self.yennemi1][self.xennemi1]='.'
                    self.yennemi1=self.yennemi1-1
                    if self.yennemi1<6:
                                self.yennemi1=6
                    if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                        self.yennemi1=self.yennemi1+1
                        deplacementRandom=random.randint(1,2)
                        self.terrain[self.yennemi1][self.xennemi1]='.'
                        if deplacementRandom==1:
                            self.xennemi1=self.xennemi1+1
                            if self.xennemi1>18:
                                    self.xennemi1=18
                            self.terrain[self.yennemi1][self.xennemi1]='D'

                        else:
                            self.xennemi1=self.xennemi1-1
                            if self.xennemi1<6:
                                self.xennemi1=6
                            self.terrain[self.yennemi1][self.xennemi1]='D'

                if action==4:
                    # a gauche
                    self.terrain[self.yennemi1][self.xennemi1]='.'
                    self.xennemi1=self.xennemi1-1
                    if self.xennemi1<6:
                                self.xennemi1=6
                    if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                        self.xennemi1=self.xennemi1+1
                        deplacementRandom=random.randint(1,2)
                        self.terrain[self.yennemi1][self.xennemi1]='.'
                        if deplacementRandom==1:
                            self.yennemi1=self.yennemi1+1
                            if self.yennemi1>16 :
                                self.yennemi1=16
                            self.terrain[self.yennemi1][self.xennemi1]='D'

                        else:
                            self.yennemi1=self.yennemi1-1
                            if self.yennemi1<6:
                                self.yennemi1=6
                            self.terrain[self.yennemi1][self.xennemi1]='D'

            else:
                if (self.yennemi1!=self.y or self.xennemi1!=self.x) :
                    action=random.randint(1,2)

                    if self.yennemi1==self.y:
                        diff=(self.x)-(self.xennemi1)

                        if diff<0:
                            # a gauche
                            self.terrain[self.yennemi1][self.xennemi1]='.'
                            self.xennemi1=self.xennemi1-1
                            if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                self.xennemi1=self.xennemi1+1
                                deplacementRandom=random.randint(1,2)
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                if deplacementRandom==1:
                                    self.yennemi1=self.yennemi1+1
                                    if self.yennemi1>16 :
                                        self.yennemi1=16
                                    self.terrain[self.yennemi1][self.xennemi1]='D'

                                else:
                                    self.yennemi1=self.yennemi1-1
                                    if self.yennemi1<6:
                                        self.yennemi1=6
                                    self.terrain[self.yennemi1][self.xennemi1]='D'
                        elif diff>0:
                            # a droite
                            self.terrain[self.yennemi1][self.xennemi1]='.'
                            self.xennemi1=self.xennemi1+1
                            if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                self.xennemi1=self.xennemi1-1
                                deplacementRandom=random.randint(1,2)
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                if deplacementRandom==1:
                                    self.yennemi1=self.yennemi1+1
                                    if self.yennemi1>16 :
                                        self.yennemi1=16
                                    self.terrain[self.yennemi1][self.xennemi1]='D'

                                else:
                                    self.yennemi1=self.yennemi1-1
                                    if self.yennemi1<6:
                                        self.yennemi1=6
                                    self.terrain[self.yennemi1][self.xennemi1]='D'




                    elif self.xennemi1==self.x:
                        diff=(self.y)-(self.yennemi1)
                        if diff<0:
                            # en haut
                            self.terrain[self.yennemi1][self.xennemi1]='.'
                            self.yennemi1=self.yennemi1-1
                            if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                self.yennemi1=self.yennemi1+1
                                deplacementRandom=random.randint(1,2)
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                if deplacementRandom==1:
                                    self.xennemi1=self.xennemi1+1
                                    if self.xennemi1>18:
                                            self.xennemi1=18
                                    self.terrain[self.yennemi1][self.xennemi1]='D'

                                else:
                                    self.xennemi1=self.xennemi1-1
                                    if self.xennemi1<6:
                                        self.xennemi1=6
                                    self.terrain[self.yennemi1][self.xennemi1]='D'


                        elif diff>0:
                            # en bas
                            self.terrain[self.yennemi1][self.xennemi1]='.'
                            self.yennemi1=self.yennemi1+1
                            if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                self.yennemi1=self.yennemi1-1
                                deplacementRandom=random.randint(1,2)
                                self.terrain[self.yennemi1][self.xennemi1]='.'

                                if deplacementRandom==1:
                                    self.xennemi1=self.xennemi1+1
                                    if self.xennemi1>18:
                                            self.xennemi1=18
                                    self.terrain[self.yennemi1][self.xennemi1]='D'
                                else:
                                    self.xennemi1=self.xennemi1-1
                                    if self.xennemi1<6:
                                        self.xennemi1=6
                                    self.terrain[self.yennemi1][self.xennemi1]='D'



                    else:
                        if action==1:
                            diff=(self.x)-(self.xennemi1)
                            if diff<0:
                                # a gauche
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                self.xennemi1=self.xennemi1-1
                                if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                    self.xennemi1=self.xennemi1+1
                                    deplacementRandom=random.randint(1,2)
                                    self.terrain[self.yennemi1][self.xennemi1]='.'
                                    if deplacementRandom==1:
                                        self.yennemi1=self.yennemi1+1
                                        if self.yennemi1>16 :
                                            self.yennemi1=16
                                        self.terrain[self.yennemi1][self.xennemi1]='D'

                                    else:
                                        self.yennemi1=self.yennemi1-1
                                        if self.yennemi1<6:
                                            self.yennemi1=6
                                        self.terrain[self.yennemi1][self.xennemi1]='D'
                            elif diff>0:
                                # a droite
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                self.xennemi1=self.xennemi1+1
                                if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                    self.xennemi1=self.xennemi1-1
                                    deplacementRandom=random.randint(1,2)
                                    self.terrain[self.yennemi1][self.xennemi1]='.'
                                    if deplacementRandom==1:
                                        self.yennemi1=self.yennemi1+1
                                        if self.yennemi1>16 :
                                            self.yennemi1=16
                                        self.terrain[self.yennemi1][self.xennemi1]='D'

                                    else:
                                        self.yennemi1=self.yennemi1-1
                                        if self.yennemi1<6:
                                            self.yennemi1=6
                                        self.terrain[self.yennemi1][self.xennemi1]='D'


                        elif action==2:
                            diff=(self.y)-(self.yennemi1)
                            if diff<0:
                                 # en haut
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                self.yennemi1=self.yennemi1-1
                                if self.terrain[self.yennemi1][self.xennemi1]=='b' or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                    self.yennemi1=self.yennemi1+1
                                    deplacementRandom=random.randint(1,2)
                                    self.terrain[self.yennemi1][self.xennemi1]='.'

                                    if deplacementRandom==1:
                                        self.xennemi1=self.xennemi1+1
                                        if self.xennemi1>18:
                                                self.xennemi1=18
                                        self.terrain[self.yennemi1][self.xennemi1]='D'
                                    else:
                                        self.xennemi1=self.xennemi1-1
                                        if self.xennemi1<6:
                                            self.xennemi1=6
                                        self.terrain[self.yennemi1][self.xennemi1]='D'
                            elif diff>0:
                                 # en bas
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                self.yennemi1=self.yennemi1+1
                                if self.terrain[self.yennemi1][self.xennemi1]=='b' or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                    self.yennemi1=self.yennemi1-1
                                    deplacementRandom=random.randint(1,2)
                                    self.terrain[self.yennemi1][self.xennemi1]='.'

                                    if deplacementRandom==1:
                                        self.xennemi1=self.xennemi1+1
                                        if self.xennemi1>18:
                                                self.xennemi1=18
                                        self.terrain[self.yennemi1][self.xennemi1]='D'
                                    else:
                                        self.xennemi1=self.xennemi1-1
                                        if self.xennemi1<6:
                                            self.xennemi1=6
                                        self.terrain[self.yennemi1][self.xennemi1]='D'
        if self.tirage==4:
            if (self.yennemi1!=self.y or self.xennemi1!=self.x) :
                    action=random.randint(1,2)
                    if self.yennemi1==self.y:
                        diff=(self.x)-(self.xennemi1)
                        if diff<0:
                            # a gauche
                            self.terrain[self.yennemi1][self.xennemi1]='.'
                            self.xennemi1=self.xennemi1-1
                            if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                self.xennemi1=self.xennemi1+1
                                deplacementRandom=random.randint(1,2)
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                if deplacementRandom==1:
                                    self.yennemi1=self.yennemi1+1
                                    if self.yennemi1>16 :
                                        self.yennemi1=16
                                    self.terrain[self.yennemi1][self.xennemi1]='D'

                                else:
                                    self.yennemi1=self.yennemi1-1
                                    if self.yennemi1<6:
                                        self.yennemi1=6
                                    self.terrain[self.yennemi1][self.xennemi1]='D'
                        elif diff>0:
                            # a droite
                            self.terrain[self.yennemi1][self.xennemi1]='.'
                            self.xennemi1=self.xennemi1+1
                            if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                self.xennemi1=self.xennemi1-1
                                deplacementRandom=random.randint(1,2)
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                if deplacementRandom==1:
                                    self.yennemi1=self.yennemi1+1
                                    if self.yennemi1>16 :
                                        self.yennemi1=16
                                    self.terrain[self.yennemi1][self.xennemi1]='D'

                                else:
                                    self.yennemi1=self.yennemi1-1
                                    if self.yennemi1<6:
                                        self.yennemi1=6
                                    self.terrain[self.yennemi1][self.xennemi1]='D'




                    elif self.xennemi1==self.x:
                        diff=(self.y)-(self.yennemi1)
                        if diff<0:
                            # en haut
                            self.terrain[self.yennemi1][self.xennemi1]='.'
                            self.yennemi1=self.yennemi1-1
                            if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                self.yennemi1=self.yennemi1+1
                                deplacementRandom=random.randint(1,2)
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                if deplacementRandom==1:
                                    self.xennemi1=self.xennemi1+1
                                    if self.xennemi1>18:
                                            self.xennemi1=18
                                    self.terrain[self.yennemi1][self.xennemi1]='D'

                                else:
                                    self.xennemi1=self.xennemi1-1
                                    if self.xennemi1<6:
                                        self.xennemi1=6
                                    self.terrain[self.yennemi1][self.xennemi1]='D'


                        elif diff>0:
                            # en bas
                            self.terrain[self.yennemi1][self.xennemi1]='.'
                            self.yennemi1=self.yennemi1+1
                            if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                self.yennemi1=self.yennemi1-1
                                deplacementRandom=random.randint(1,2)
                                self.terrain[self.yennemi1][self.xennemi1]='.'

                                if deplacementRandom==1:
                                    self.xennemi1=self.xennemi1+1
                                    if self.xennemi1>18:
                                            self.xennemi1=18
                                    self.terrain[self.yennemi1][self.xennemi1]='D'
                                else:
                                    self.xennemi1=self.xennemi1-1
                                    if self.xennemi1<6:
                                        self.xennemi1=6
                                    self.terrain[self.yennemi1][self.xennemi1]='D'



                    else:
                        if action==1:
                            diff=(self.x)-(self.xennemi1)
                            if diff<0:
                                # a gauche
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                self.xennemi1=self.xennemi1-1
                                if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                    self.xennemi1=self.xennemi1+1
                                    deplacementRandom=random.randint(1,2)
                                    self.terrain[self.yennemi1][self.xennemi1]='.'
                                    if deplacementRandom==1:
                                        self.yennemi1=self.yennemi1+1
                                        if self.yennemi1>16 :
                                            self.yennemi1=16
                                        self.terrain[self.yennemi1][self.xennemi1]='D'

                                    else:
                                        self.yennemi1=self.yennemi1-1
                                        if self.yennemi1<6:
                                            self.yennemi1=6
                                        self.terrain[self.yennemi1][self.xennemi1]='D'
                            elif diff>0:
                                # a droite
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                self.xennemi1=self.xennemi1+1
                                if self.terrain[self.yennemi1][self.xennemi1]=="b" or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                    self.xennemi1=self.xennemi1-1
                                    deplacementRandom=random.randint(1,2)
                                    self.terrain[self.yennemi1][self.xennemi1]='.'
                                    if deplacementRandom==1:
                                        self.yennemi1=self.yennemi1+1
                                        if self.yennemi1>16 :
                                            self.yennemi1=16
                                        self.terrain[self.yennemi1][self.xennemi1]='D'

                                    else:
                                        self.yennemi1=self.yennemi1-1
                                        if self.yennemi1<6:
                                            self.yennemi1=6
                                        self.terrain[self.yennemi1][self.xennemi1]='D'


                        elif action==2:
                            diff=(self.y)-(self.yennemi1)
                            if diff<0:
                                 # en haut
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                self.yennemi1=self.yennemi1-1
                                if self.terrain[self.yennemi1][self.xennemi1]=='b' or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                    self.yennemi1=self.yennemi1+1
                                    deplacementRandom=random.randint(1,2)
                                    self.terrain[self.yennemi1][self.xennemi1]='.'

                                    if deplacementRandom==1:
                                        self.xennemi1=self.xennemi1+1
                                        if self.xennemi1>18:
                                                self.xennemi1=18
                                        self.terrain[self.yennemi1][self.xennemi1]='D'
                                    else:
                                        self.xennemi1=self.xennemi1-1
                                        if self.xennemi1<6:
                                            self.xennemi1=6
                                        self.terrain[self.yennemi1][self.xennemi1]='D'
                            elif diff>0:
                                 # en bas
                                self.terrain[self.yennemi1][self.xennemi1]='.'
                                self.yennemi1=self.yennemi1+1
                                if self.terrain[self.yennemi1][self.xennemi1]=='b' or self.terrain[self.yennemi1][self.xennemi1]=='+' or self.terrain[self.yennemi1][self.xennemi1]=='e':
                                    self.yennemi1=self.yennemi1-1
                                    deplacementRandom=random.randint(1,2)
                                    self.terrain[self.yennemi1][self.xennemi1]='.'

                                    if deplacementRandom==1:
                                        self.xennemi1=self.xennemi1+1
                                        if self.xennemi1>18:
                                                self.xennemi1=18
                                        self.terrain[self.yennemi1][self.xennemi1]='D'
                                    else:
                                        self.xennemi1=self.xennemi1-1
                                        if self.xennemi1<6:
                                            self.xennemi1=6
                                        self.terrain[self.yennemi1][self.xennemi1]='D'
        if self.tirage!=0:
            self.terrain[self.yennemi1][self.xennemi1]='D'
            game.timer()
            print(self.score)
            game.stageactive()


    def Ennemi_placement(self):
        self.yennemi1=random.randint(6,16)
        self.xennemi1=random.randint(6,18)
        while self.terrain[self.yennemi1][self.xennemi1]!='.':
            self.yennemi1=random.randint(6,16)
            self.xennemi1=random.randint(6,18)
        self.terrain[self.yennemi1][self.xennemi1]='D'
        self.stageactive()
        print("")
        self.tirage=4

    def bonus_spawn(self):
        for i in range(0,5):
            yscore=random.randint(6,16)
            xscore=random.randint(6,18)
            while self.terrain[yscore][xscore]!='.':
                yscore=random.randint(6,16)
                xscore=random.randint(6,18)
            self.terrain[yscore][xscore]='+'
        game.stageactive()

    def fruits(self):
        #Apple,Pineapple,Orange,riceball,meat,jelly,ice cream,takoyaki
        liste=["A","P","O","R","M","J","I","T"]
        for i in range(len(liste)):
            yscore=random.randint(6,16)
            xscore=random.randint(6,18)
            while self.terrain[yscore][xscore]!='.':
                yscore=random.randint(6,16)
                xscore=random.randint(6,18)
            self.terrain[yscore][xscore]=liste[i]
        self.stageactive()

    def timer(self):
            print(self.temporaliter_m,":",self.temporaliter_s)
    def Game(self):
        game_running=True
        bombe_restriction=0
        evt=pygame.USEREVENT+1
        evt_temp=pygame.USEREVENT+2
        evt_ennemi=pygame.USEREVENT+3
        evt_tps=pygame.USEREVENT+4
        evt_sprint=pygame.USEREVENT+5
        sprinteur=2000

        # initialisation du timer monstre
        pygame.time.set_timer(evt_ennemi, 2000)
        pygame.time.set_timer(evt_sprint, sprinteur)
        pygame.time.set_timer(evt_tps, 1000)
        while game_running:
            bombe_lvl=game.bombe()
            if self.terrain[self.y][self.x]=="e"or self.terrain[self.y][self.x]=="D" :
                game.gameover()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    game_running = False

                if event.type == evt_sprint:
                        if self.tirage==4:
                            game.Ennemi_comportement1()
                            if self.temporaliter_s ==59:
                                sprinteur=sprinteur-500
                                print(sprinteur)
                                pygame.time.set_timer(evt_sprint, sprinteur)
                            if sprinteur<500:
                                sprinteur=500
                                pygame.time.set_timer(evt_sprint, sprinteur)

                if event.type == evt_tps:
                    if self.temporaliter_s<59:
                        self.temporaliter_s=self.temporaliter_s+1
                    else:
                        self.temporaliter_m=self.temporaliter_m+1
                        self.temporaliter_s=self.temporaliter_s=0
                    game.timer()
                    print(self.score)
                    game.stageactive()
                if event.type == evt_ennemi:
                    if self.tirage!=4:
                        game.Ennemi_comportement1()

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
                    self.terrain[y][x]='.'
                    self.terrain[y+1][x]='.'
                    self.terrain[y-1][x]='.'
                    self.terrain[y][x+1]='.'
                    self.terrain[y][x-1]='.'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,0)
                    bombe_restriction=0
                if event.type==evt_temp  and bombe_lvl ==1:
                    print(self.score)
                    self.terrain[y][x]='.'
                    self.terrain[y+1][x]='.'
                    self.terrain[y-1][x]='.'
                    self.terrain[y][x+1]='.'
                    self.terrain[y][x-1]='.'
                    self.terrain[y+2][x]='.'
                    self.terrain[y-2][x]='.'
                    self.terrain[y][x+2]='.'
                    self.terrain[y][x-2]='.'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,0)
                    bombe_restriction=0
                if event.type==evt_temp  and bombe_lvl ==2:
                    print(self.score)
                    self.terrain[y][x]='.'
                    self.terrain[y+1][x]='.'
                    self.terrain[y-1][x]='.'
                    self.terrain[y][x+1]='.'
                    self.terrain[y][x-1]='.'
                    self.terrain[y+2][x]='.'
                    self.terrain[y-2][x]='.'
                    self.terrain[y][x+2]='.'
                    self.terrain[y][x-2]='.'
                    self.terrain[y+3][x]='.'
                    self.terrain[y-3][x]='.'
                    self.terrain[y][x+3]='.'
                    self.terrain[y][x-3]='.'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,0)
                    bombe_restriction=0
                if event.type==evt_temp  and bombe_lvl ==3:
                    print(self.score)
                    self.terrain[y][x]='.'
                    self.terrain[y+1][x]='.'
                    self.terrain[y-1][x]='.'
                    self.terrain[y][x+1]='.'
                    self.terrain[y][x-1]='.'
                    self.terrain[y+2][x]='.'
                    self.terrain[y-2][x]='.'
                    self.terrain[y][x+2]='.'
                    self.terrain[y][x-2]='.'
                    self.terrain[y+3][x]='.'
                    self.terrain[y-3][x]='.'
                    self.terrain[y][x+3]='.'
                    self.terrain[y][x-3]='.'
                    self.terrain[y+4][x]='.'
                    self.terrain[y-4][x]='.'
                    self.terrain[y][x+4]='.'
                    self.terrain[y][x-4]='.'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,0)
                    bombe_restriction=0
                if event.type==evt_temp  and bombe_lvl ==4:
                    print(self.score)
                    self.terrain[y][x]='.'
                    self.terrain[y+1][x]='.'
                    self.terrain[y-1][x]='.'
                    self.terrain[y][x+1]='.'
                    self.terrain[y][x-1]='.'
                    self.terrain[y+2][x]='.'
                    self.terrain[y-2][x]='.'
                    self.terrain[y][x+2]='.'
                    self.terrain[y][x-2]='.'
                    self.terrain[y+3][x]='.'
                    self.terrain[y-3][x]='.'
                    self.terrain[y][x+3]='.'
                    self.terrain[y][x-3]='.'
                    self.terrain[y+4][x]='.'
                    self.terrain[y-4][x]='.'
                    self.terrain[y][x+4]='.'
                    self.terrain[y][x-4]='.'
                    self.terrain[y+5][x]='.'
                    self.terrain[y-5][x]='.'
                    self.terrain[y][x+5]='.'
                    self.terrain[y][x-5]='.'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,0)
                    bombe_restriction=0
                if event.type==evt_temp  and bombe_lvl ==5:
                    print(self.score)
                    self.terrain[y][x]='.'
                    self.terrain[y+1][x]='.'
                    self.terrain[y-1][x]='.'
                    self.terrain[y][x+1]='.'
                    self.terrain[y][x-1]='.'
                    self.terrain[y+2][x]='.'
                    self.terrain[y-2][x]='.'
                    self.terrain[y][x+2]='.'
                    self.terrain[y][x-2]='.'
                    self.terrain[y+3][x]='.'
                    self.terrain[y-3][x]='.'
                    self.terrain[y][x+3]='.'
                    self.terrain[y][x-3]='.'
                    self.terrain[y+4][x]='.'
                    self.terrain[y-4][x]='.'
                    self.terrain[y][x+4]='.'
                    self.terrain[y][x-4]='.'
                    self.terrain[y+5][x]='.'
                    self.terrain[y-5][x]='.'
                    self.terrain[y][x+5]='.'
                    self.terrain[y][x-5]='.'
                    self.terrain[y+6][x]='.'
                    self.terrain[y-6][x]='.'
                    self.terrain[y][x+6]='.'
                    self.terrain[y][x-6]='.'
                    self.stageactive()
                    pygame.time.set_timer(evt_temp,0)
                    bombe_restriction=0

game=Bomberman()
game.stageactive()
game.bonus_spawn()
game.fruits()
game.initialisation()
game.Ennemi_placement()
game.Game()
pygame.quit()
