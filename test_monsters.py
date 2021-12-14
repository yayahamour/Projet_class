from sys import path
path.append("./src")
import pytest
from monster import Monster
from hero import Hero

HERO_DICT_SAMPLE = {"Heal":(2,3,10), "Fire":(0,1,5), "Ice":(1,1,6), "Lightning":(0,1,5)}
MONSTER_DICT_SAMPLE  = {"Heal":(2,3,10), "Fire":(0,6,5), "Ice":(0,0,6), "Lightning":(0,0,5)}

@pytest.fixture
def gobelin_test():
    return Monster((40, 40), 4, 1, 5, MONSTER_DICT_SAMPLE, "Gobelin", 75)

@pytest.fixture
def liche_test():
    return Monster((40, 40), 5, 1, 5, MONSTER_DICT_SAMPLE, "Liche", 75)

@pytest.fixture
def orc_test():
    return Monster((40, 40), 4, 1, 5, MONSTER_DICT_SAMPLE, "Orc", 75)

@pytest.fixture
def drake_test():
    return Monster((40, 40), 4, 1, 5, MONSTER_DICT_SAMPLE, "Drake", 75)

@pytest.fixture
def hero_test():
    return Hero((45,50), 5, 1, 5, HERO_DICT_SAMPLE, 0, 1, 50)
class TestMonster():
    
    def test_monster_var(self, gobelin_test, liche_test, orc_test, drake_test):
        assert gobelin_test._life == (40,40)
        assert gobelin_test._strength == 4
        assert gobelin_test._armor == 1
        assert gobelin_test._book == MONSTER_DICT_SAMPLE
        assert gobelin_test.rank == 'Gobelin'
        assert liche_test.rank == 'Liche'
        assert orc_test.rank == 'Orc'
        assert drake_test.rank == 'Drake'
        assert drake_test._book == {"Heal":(0,0,0), "Fire":(999,999,10), "Ice":(999,999,10), "Lightning":(999,999,10)} 
        assert gobelin_test.xp == 75
        
    def test_gobelin_turn(self, gobelin_test, hero_test):
        gobelin_test.turn(hero_test)
        assert hero_test._life[0] == 42 or hero_test._life[0] == 38
        
    def test_liche_turn(self, liche_test, hero_test):
        liche_test.turn(hero_test)
        assert hero_test._life[0] == 41 or hero_test._life[0] == 38 or hero_test._life[0] == 36 or hero_test._life[0] == 31
        
    def test_orc_turn(self, orc_test, hero_test):
        orc_test.turn(hero_test)
        assert hero_test._life[0] == 39 or hero_test._life[0] == 35 or hero_test._life[0] == 31