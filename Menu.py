import os
import time


INTRO = """Lors du première épisode, notre valeureux héro est mort en veins,
il n'était pas si valeureux en faite. Mais cette fois ci, arriverez-vous à surmonter nos épreuves ?
WELCOME TO THE MORTAL KKKKOMBAT .....
    euh ah nan c'est le Brightest Dungeon 2 Anniversary Collector Deluxe Edition \n"""

ENTRER = """Vous avez décidez de vous aventurez dans ce donjon comme bien d'autre aventurier avant vous
peut-être aurez-vous plus de chance\n"""

OBJET_CAMP = """Visiblement un de vos prédécesseurs vous à laissé quelque chose\n"""

OBJET_ENEMY = """Vous récuperez un objet sur le cadavre d'un monstre"""

ETAGE_SUIVANT = """Un étage de fait au suivant"""

ENEMY1 = """Des enemies vous barre la route affronter les pour continuer"""

ENEMY2 = """Des enemies sont la à vous de jouer"""

STAGE_1 = """Un Goblin vous acceuil, c'est votre jour de chance mais méfiez vous
Les prochains étages ne seront surement pas aussi facile\n"""

FIRST_BOSS = """Un Orc se dresse devant vous, je vous avez prévenu\n"""

FINAL_BOSS = """U..UUUNN... UUUUNNNN DRAAAAAAGGGGOONNNN FUUUUYYYEEZZZ\n"""

CAMP = """On dirais que cette endroit est parfait pour vous reposez

.........
Vous êtes prêt à reprendre l'aventure"""

GENERIQUE = """\t\tBrightest Dungeon 2 Anniversary Collector Deluxe Edition


\tMerci d'avoir jouer

\tCreé par : Florian et Yanis

\tStory telling :Florian et Yanis

\tGraphisme : Florian et Yanis

\tSon : Florian et Yanis

\tEffet spéciaux : Florian et Yanis

\tActeur principal : Florian

\tFaute d'orthographe : Yanis

\tRemerciement spéciaux : Charles"""
class Menu:

    def principal(self, book):
        i = 2
        tab = ["Attaque"]
        print("Quel action voulez-vous faire :\n",
                "1 : Attaque simple")
        nb_spell = book["Heal"][0]
        if(nb_spell > 0):
            power = book["Heal"][2]
            print(f" {i} : Utiliser Heal, {nb_spell} Utilisation disponible (+{power} pv)") 
            i += 1
        nb_spell = book["Fire"][0]
        if(nb_spell > 0):
            power = book["Fire"][2]
            print(f" {i} : Utiliser Fire, {nb_spell} Utilisation disponible ({power} dmg)")
            i += 1 
        nb_spell = book["Lightning"][0]
        if(nb_spell > 0):
            power = book["Lightning"][2]
            print(f" {i} : Utiliser Lightning, {nb_spell} Utilisation disponible ({power} dmg)")
            i += 1
        if(nb_spell > 0):
            power = book["Ice"][2]
            print(f" {i} : Utiliser Ice, {nb_spell} Utilisation disponible ({power} dmg)")
            i += 1
        print(
                f" {i} : Sauvegarder\n",
                f"{i+1} : Quitter")
    
    def story(self, var):
        for i in range(0, len(var)):
            time.sleep(0.04)
            print(var[i], end='')

os.system("cls")            
my_menu = Menu()        


my_menu.story(INTRO)

time.sleep(1)
os.system("cls")
my_menu.story(ENTRER)

time.sleep(1)
os.system("cls")
my_menu.story(STAGE_1)

time.sleep(1)
os.system("cls")
my_menu.story(ETAGE_SUIVANT)

time.sleep(1)
os.system("cls")
my_menu.story(ENEMY1)

time.sleep(1)
os.system("cls")
my_menu.story(OBJET_ENEMY)


time.sleep(1)
os.system("cls")
my_menu.story(ETAGE_SUIVANT)

time.sleep(1)
os.system("cls")
my_menu.story(ENEMY2)

time.sleep(1)
os.system("cls")
my_menu.story(ETAGE_SUIVANT)

time.sleep(1)
os.system("cls")
my_menu.story(FIRST_BOSS)

time.sleep(1)
os.system("cls")
my_menu.story(ETAGE_SUIVANT)

time.sleep(1)
os.system("cls")
my_menu.story(CAMP)

time.sleep(1)
os.system("cls")
my_menu.story(OBJET_CAMP)

time.sleep(1)
os.system("cls")
my_menu.story(ETAGE_SUIVANT)

time.sleep(1)
os.system("cls")
my_menu.story(FINAL_BOSS)

time.sleep(1)
os.system("cls")
my_menu.story(GENERIQUE)


my_menu.principal({"Heal":(3,4,10), "Fire":(0,5,5), "Ice":(1,4,5), "Lightning":(1,5,5)})

