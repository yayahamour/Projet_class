import pytest
from Monster import Monster
from Hero import Hero

HERO_DICT_SAMPLE = {"Heal":(2,3,10), "Fire":(0,1,5), "Ice":(1,1,6), "Lightning":(0,1,5)}
MONSTER_DICT_SAMPLE  = {"Heal":(2,3,10), "Fire":(0,6,5), "Ice":(0,0,6), "Lightning":(0,0,5)}

@pytest.fixture
def gobelin_test():
    return Monster((40, 40), 4, 1, MONSTER_DICT_SAMPLE, "Gobelin", 75)
@pytest.fixture
def liche_test():
    return Monster((40, 40), 5, 1, MONSTER_DICT_SAMPLE, "Liche", 75)
@pytest.fixture
def boss_test():
    return Monster((40, 40), 6, 1, MONSTER_DICT_SAMPLE, "Boss", 75)
@pytest.fixture
def hero_test():
    return Hero((45,50), 5, 1, HERO_DICT_SAMPLE, 0, 1, 50)
class TestMonster():
    
    def test_monster_var(self, gobelin_test, liche_test, boss_test):
        assert gobelin_test._life == (40,40)
        assert gobelin_test._strength == 4
        assert gobelin_test._armor == 1
        assert gobelin_test._book == MONSTER_DICT_SAMPLE
        assert gobelin_test.rank == 'Gobelin'
        assert liche_test.rank == 'Liche'
        assert boss_test.rank == 'Boss'
        assert gobelin_test.xp == 75
        
    def test_turn(self, gobelin_test, hero_test, liche_test, boss_test):
        gobelin_test.turn(hero_test)
        assert hero_test._life[0] == 42
        liche_test.turn(hero_test)
        assert hero_test._life[0] == 38 or hero_test._life[0] == 37
        boss_test.turn(hero_test)
        assert hero_test._life[0] == 28 or hero_test._life[0] == 27