from dataclasses import dataclass, field
import os
from typing import List
from monster import Monster
from hero import Hero
from display import *
from random import randint
import re


@dataclass
class Game():
    player : Hero = Hero((50,50), 5, 0, 5, {"Heal":(3,3,10), "Fire":(0,0,5), "Ice":(0,0,7), "Lightning":(0,0,10)}, 0, 1, 50)
    display : Display = Display()
    monsters : list = field(default_factory=list)
    stage : int = 1
   
    def next_stage(self):
        self.stage += 1
        self.display.story("Vous montez longuement un escalier en collimasson pour arriver à l'étage suivant")
        self.display.story(f"Vous arrivez à l'étage {self.stage}")


        nb = 1
        if (self.stage > 6 and self.stage % 5 == 1):
            self.player.camp()
        if ((self.stage % 10) == 0):
            self.display.story(FINAL_BOSS)
            self.monsters.append(Monster((100,100),10,5,5,{},"Drake", 1000))
        elif ((self.stage % 5) == 0):
            self.display.story(FIRST_BOSS)
            self.monsters.append(Monster((40,40),3,2,2,{},"Orc", 500))
        else :
            if self.stage > 5 and self.stage < 10:
                nb = 2
            elif self.stage > 10:
                nb = 3
            for i in range(0, nb):
                rand = randint(1,100)
                if(rand >= 70):
                    self.monsters.append(Monster((10,10),1,0,2,{},"Liche", 40))
                else:
                    self.monsters.append(Monster((5,5),2,0,1,{},"Gobelin", 25))

    def game(self):
        playing = True
        turn_player = True
        time_before_loose = 0
        while (playing):
            if (len(self.monsters) == 0):
                self.next_stage()
            while(turn_player and time_before_loose < 4):
                self.display.turn_menu(self.player._book, self.player._strength)
                _input = input("Choix : ")
                try:
                    case = int(_input)
                    if(self.player.turn(case, self.monsters)):
                        turn_player = False
                        time_before_loose = 0

                    else:
                        time_before_loose += 1
                except:
                    time_before_loose += 1
            for monster in self.monsters:
                monster.turn(self.player)
            turn_player = True
            if(self.player._life[0] <= 0):
                self.display.story(GENERIQUE)
                playing = False
            



    def start(self):
        # os.system('cls')
        # self.menu.story(INTRO)
        # os.system('cls')

        # self.menu.story(ENTRER)
        # os.system('cls')
        # time.sleep(0.5)
        # self.menu.story(STAGE_1)
        self.monsters.append(Monster((3, 3), 4, 1, 0, {}, "Gobelin", 1))
        self.game()


game = Game()
game.start()
