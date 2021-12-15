from sys import path
import pymongo
path.append("./src")
from dataclasses import dataclass
import os
from game import Game

class Main():

   def display_save(self):
      """[Display all saves]

      Returns:
          [list]: [list of save id]
      """
      my_client = pymongo.MongoClient('mongodb://localhost:27017/')
      my_db = my_client['playersaves']
      my_character = my_db['character']
      my_saves = my_character.find({}, {'id':1, '_id':0})
      cnt = 0
      tab_id = []
      os.system("cls")
      for i in my_saves:
         cnt += 1
         tab_id.append(i['id'])
         print(f"{cnt} : {tab_id[cnt-1]}")
      print(f'{cnt + 1}: Annuler')
      return tab_id

   def main(self):
      """[Start the script of the game]
      """
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
            elif(_input == 2 or _input == 3):
               tab_id = self.display_save()
               save_choice = input("Choix : ")
               try: 
                  save_choice = int(save_choice)
                  if len(tab_id) > (save_choice - 1):
                     save_name = tab_id[save_choice - 1]
                     if(_input == 2):
                        game.load(save_name)
                     else:
                        game.delete_save(save_name)
                  else:
                     os.system("cls")
                     pass
               except:
                  os.system("cls")
                  time_before_quit += 1
                  print("Entrer une valeur correct")
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

Main().main()