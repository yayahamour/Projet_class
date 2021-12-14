import pytest
from display import Display
from hero import Hero
from monster import Monster

HERO_DICT_SAMPLE = {"Heal":(2,3,10), "Fire":(0,1,5), "Ice":(0,1,6), "Lightning":(1,1,5)}
MONSTER_DICT_SAMPLE  = {"Heal":(2,3,10), "Fire":(0,0,5), "Ice":(0,0,6), "Lightning":(0,0,5)}

@pytest.fixture
def hero_test():
    return Hero((45,50), 5, 1, 5, HERO_DICT_SAMPLE, 0, 1, 50)

@pytest.fixture
def display_test():
    return Display()

pytest.fixture
def mob_list_test():
    mob_list = []
    mob1 = Monster((40, 40), 10, 1, 5, MONSTER_DICT_SAMPLE, "Gobelin", 75)
    mob2 = Monster((40, 40), 10, 1, 5, MONSTER_DICT_SAMPLE, "Gobelin", 75)
    mob_list.append(mob1, mob2)
    return mob_list
class TestDisplay:
    
    def test_display_stats(self, display_test, hero_test, capsys):
        display_test.display_stats(hero_test)
        strout = ["******** Statistiques ******** \n",
                  "Niveau : 1",
                  "Expérience : 0 / 50",
                  "Point de vie : 45 / 50",
                  "Force : 5",
                  "Armure : 1",
                  "Chance de coup critique : 5",
                  "******** ------------ ********\n"]
        assert capsys.readouterr().out == "".join(strout)
        
    def test_display_stats(self, display_test, mob_list, capsys):
        display_test.display_enemies(mob_list)
        assert capsys.readouterr().out == "Gobelin : 40 / 40 PV", "Gobelin : 40 / 40 PV"