import pytest
from display import Display, FINAL_BOSS
from hero import Hero
from monster import Monster

HERO_DICT_SAMPLE = {"Heal":(2,3,10), "Fire":(0,1,5), "Ice":(0,1,6), "Lightning":(1,1,5)}
MONSTER_DICT_SAMPLE  = {"Heal":(2,3,10), "Fire":(0,6,5), "Ice":(0,0,6), "Lightning":(0,0,5)}

@pytest.fixture
def gobelin_test():
    return [Monster((40, 40), 4, 1, 5, MONSTER_DICT_SAMPLE, "Gobelin", 75)]

@pytest.fixture
def hero_test():
    return Hero((45,50), 5, 1, 5, HERO_DICT_SAMPLE, 0, 1, 50)
@pytest.fixture
def display_test():
    return Display()
class TestDisplay:

    def test_display_enemie(self, display_test, gobelin_test, capsys):
        display_test.display_enemies(gobelin_test)
        assert capsys.readouterr().out == "Gobelin : 40 / 40 PV\n"

    def test_display_stats(self, display_test,hero_test, capsys):
        strout = ["******** Statistiques ******** \n\n",
                    "Niveau : 1\n",
                    "Expérience : 0 / 50\n",
                    "Point de vie : 45 / 50\n",
                    "Force : 5\n",
                    "Armure : 1\n",
                    "Chance de coup critique : 5\n\n",
                    "******** ------------ ********\n\n"]
        display_test.display_stats(hero_test)
        assert capsys.readouterr().out == "".join(strout)

    def test_display_menu(self, display_test,hero_test, capsys):

        display_test.turn_menu({"Heal":(3,4,10), "Fire":(0,5,5), "Ice":(1,4,5), "Lightning":(1,5,5)}, 5)
        strout = ["Quel action voulez-vous faire :\n",
                    " 1 : Attaque simple (5 dmg)\n",
                    " 2 : Utiliser Heal, 3 Utilisation disponible (+10 pv)\n",
                    " 3 : Utiliser Fire, 0 Utilisation disponible (5 dmg)\n",
                    " 4 : Utiliser Lightning, 1 Utilisation disponible (5 dmg)\n",
                    " 5 : Utiliser Ice, 1 Utilisation disponible (5 dmg)\n",
                    " 6 : Quitter\n"]
        assert capsys.readouterr().out == "".join(strout)
        display_test.story(FINAL_BOSS)
        assert capsys.readouterr().out == "U..UUUNN... UUUUNNNN DRAAAAAAGGGGOONNNN FUUUUYYYEEZZZ\n"
        display_test.principal_menu()
        assert capsys.readouterr().out == "".join(["1 : Nouvelle Partie\n",
              "2 : Charger Partie\n",
              "3 : Supprimer Partie\n",
              "4 : Quitter"])