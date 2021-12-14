from sys import path
path.append("./src")
from dataclasses import dataclass
import os
from game import Game



def main():
   
   game = Game()
   playing = True
 
   time_before_quit = 0
   os.system("cls")
   while(playing and time_before_quit < 4):
     
      game.display.principal_menu()
      _input = input("Choix : ")
      try:
         _input = int(_input)
         if (_input == 1):
            game.start()
         elif(_input == 2):
            pass
         elif(_input == 3):
            pass
         elif (_input == 4):
            playing = False
         else :
            os.system("cls")
            print("Entrer valeur correct")
            time_before_quit += 1
      except:
         os.system("cls")
         time_before_quit += 1
         print("Entrer valeur correct")
main()