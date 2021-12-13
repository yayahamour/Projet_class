import pytest
from menu import FINAL_BOSS, Menu
import sys

@pytest.fixture
def menu_test():
    return Menu()

class TestMenu():

    def test_menu(self, menu_test, capsys):
        menu_test.turn_menu({"Heal":(3,4,10), "Fire":(0,5,5), "Ice":(1,4,5), "Lightning":(1,5,5)}, 5)
        strout = ["Quel action voulez-vous faire :\n",
                    " 1 : Attaque simple (5 dmg)\n",
                    " 2 : Utiliser Heal, 3 Utilisation disponible (+10 pv)\n",
                    " 3 : Utiliser Fire, 0 Utilisation disponible (5 dmg)\n",
                    " 4 : Utiliser Lightning, 1 Utilisation disponible (5 dmg)\n",
                    " 5 : Utiliser Ice, 1 Utilisation disponible (5 dmg)\n",
                    " 6 : Sauvegarder\n",
                    " 7 : Quitter\n"]
        assert capsys.readouterr().out == "".join(strout)
        menu_test.story(FINAL_BOSS)
        assert capsys.readouterr().out == "U..UUUNN... UUUUNNNN DRAAAAAAGGGGOONNNN FUUUUYYYEEZZZ\n"
        menu_test.principal_menu()
        assert capsys.readouterr().out == "1 : Nouvelle Partie\n2 : Quitter\n"