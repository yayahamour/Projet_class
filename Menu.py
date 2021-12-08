import os
import time

INTRO = """Lors du première épisode, notre valeureux héro est mort en veins,
il n'était pas si valeureux en faite. Mais cette fois ci, arriverez-vous à surmonter nos épreuves ?
WELCOME TO THE MORTAL KKKKOMBAT .....
    euh ah nan c'est le Brightest Dungeon 2 Anniversary Collector Deluxe Edition """
ACT1 = """ACT One"""
class Menu:
    
    def story(self, var):
        os.system("cls")
        for i in range(0, len(var)+1):
            time.sleep(0.01)
            os.system("cls")
            print(var[:i])
            
my_menu = Menu()          
my_menu.story(INTRO)
