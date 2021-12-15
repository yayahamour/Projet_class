import os
import time

INTRO = """Lors du première épisode, notre valeureux héro est mort en veins,
il n'était pas si valeureux en faite. Mais cette fois ci, arriverez-vous à surmonter nos épreuves ?
WELCOME TO THE MORTAL KKKKOMBAT .....
    euh ah nan c'est le Brightest Dungeon 2 Anniversary Collector Deluxe Edition \n"""

ENTRER = """Vous avez décidez de vous aventurez dans ce donjon comme bien d'autre aventurier avant vous
peut-être aurez-vous plus de chance\n"""

OBJET = """Visiblement un de vos prédécesseurs vous à laissé quelque chose\n"""

STAGE_1 = """Un Goblin vous acceuil, c'est votre jour de chance mais méfiez vous
Les prochains étages ne seront surement pas aussi facile\n"""

FIRST_BOSS = """Un Orc se dresse devant vous, je vous avez prévenu\n"""

FINAL_BOSS = """U..UUUNN... UUUUNNNN DRAAAAAAGGGGOONNNN FUUUUYYYEEZZZ\n"""

GENERIQUE = """\t\tBrightest Dungeon 2 Anniversary Collector Deluxe Edition


\tMerci d'avoir jouer

\tCreé par : Florian et Yanis

\tStory telling :Florian et Yanis

\tGraphisme : Florian et Yanis

\tSon : Florian et Yanis

\tEffet spéciaux : Florian et Yanis

\tActeur principal : Florian

\tFaute d'orthographe : Yanis

\tRemerciement spéciaux : Charles\n"""
class Display:

    def principal_menu(self):
        print(" 1 : Nouvelle Partie\n",
              "2 : Charger Partie\n",
              "3 : Supprimer Partie\n",
              "4 : Quitter")
        
    def display_stats(self, hero):
        print('******** Statistiques ******** \n')
        print(f"Niveau : {hero.lvl}")
        print(f"Expérience : {hero.xp} / {hero.xp_lvl_up}")
        print(f"Point de vie : {hero._life[0]} / {hero._life[1]}")
        print(f"Force : {hero._strength}")
        print(f"Armure : {hero._armor}")
        print(f"Chance de coup critique : {hero._crit_rate}\n")
        print('******** ------------ ********\n')
             
    def display_enemies(self, mob_list):
        for mob in mob_list:
            print(f"{mob.rank} : {mob._life[0]} / {mob._life[1]} PV")
            
    def turn_menu(self, book, strength):
        i = 2
        print("Quel action voulez-vous faire :\n",
                f"1 : Attaque simple ({strength} dmg)")
        nb_spell = book["Heal"][0]
        power = book["Heal"][2]
        print(f" 2 : Utiliser Heal, {nb_spell} Utilisation disponible (+{power} pv)") 
        nb_spell = book["Fire"][0]
        power = book["Fire"][2]
        print(f" 3 : Utiliser Fire, {nb_spell} Utilisation disponible ({power} dmg)")
        nb_spell = book["Lightning"][0]
        power = book["Lightning"][2]
        print(f" 4 : Utiliser Lightning, {nb_spell} Utilisation disponible ({power} dmg)")
        power = book["Ice"][2]
        print(f" 5 : Utiliser Ice, {nb_spell} Utilisation disponible ({power} dmg)")
        print(" 6 : Sauvegarder")
        print(" 7 : Quitter")
    
    def story(self, var):
        for i in range(0, len(var)):
            time.sleep(0.04)
            print(var[i], end='')
        time.sleep(2)


# os.system("cls")            
# my_menu = Menu()          
# my_menu.principal({"Heal":(3,4,10), "Fire":(0,5,5), "Ice":(1,4,5), "Lightning":(1,5,5)})

