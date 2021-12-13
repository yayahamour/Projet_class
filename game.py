from dataclasses import dataclass, field
import os
from typing import List
from Monster import Monster
from Hero import Hero
from Display import *


@dataclass
class Game():
    player : Hero = Hero((50,50), 5, 0, {"Heal":(3,3,10), "Fire":(0,0,5), "Ice":(0,0,7), "Lightning":(0,0,10)}, 0, 1, 50)
    menu : Display = Display()
    monsters : list = field(default_factory=list)
    stage : int = 1
   
    def next_stage(self):
        self.stage += 1
        if ((self.stage % 10) == 0):
            #boss dragon
            pass
        elif ((self.stage % 5) == 0):
            #boss orc
            pass
        else :
            if self.stage > 5 and self.stage < 10:
                nb = 2
            elif self.stage > 10:
                nb = 3
            for i in range(0, nb):
                pass

    def game(self):
        playing = True
        turn_player = True
        time_before_loose = 0
        while (playing):
            if (len(self.monsters) == 0):
                self.next_stage()
            while(turn_player and time_before_loose < 4):
                os.system('cls')
                self._menu.turn_menu()
                _input = input("Choix : ")
                if (isinstance(int, _input)):
                    case = int(_input)
                    if(self.player.turn(case, self.monsters)):
                        turn_player = False
                    else:
                        time_before_loose += 1
                else:
                    time_before_loose += 1



    def start(self):
        os.system('cls')
        self.menu.story(INTRO)
        os.system('cls')
        self.menu.story(ENTRER)
        os.system('cls')
        self.menu.story(STAGE_1)
        self.monsters.append(Monster((3, 3), 4, 1, {}, "Gobelin", 1))
        self.game()


game = Game()
game.start()
