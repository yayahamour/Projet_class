import pytest
from Hero import Hero
from Monster import Monster

HERO_DICT_SAMPLE = {"Heal":(2,3,10), "Fire":(0,1,5), "Ice":(1,1,6), "Lightning":(0,1,5)}
MONSTER_DICT_SAMPLE  = {"Heal":(2,3,10), "Fire":(0,0,5), "Ice":(0,0,6), "Lightning":(0,0,5)}

@pytest.fixture
def monster_test():
    return Monster((40, 40), 10, 1, MONSTER_DICT_SAMPLE, "Gobelin", 75)

@pytest.fixture
def hero_test():
    return Hero((45,50), 5, 1, HERO_DICT_SAMPLE, 0, 1, 50)

class TestHero():
         
    def hero_var_test(self, hero_test):
        assert hero_test._life == (45,40)
        assert hero_test._strength == 5
        assert hero_test._armor == 1
        assert hero_test._book == {"Heal":(2,3,10), "Fire":(0,1,5), "Ice":(1,1,6), "Lightning":(0,1,5)}
        assert hero_test.xp == 0
        assert hero_test.lvl == 1
        assert hero_test.xp_lvl_up == 50        
        
    def test_camp(self, hero_test):
        hero_test.camp()
        assert hero_test._book['Heal'][0] == 3 
        assert hero_test._book['Fire'][0] == 1 
        assert hero_test._book['Ice'][0] == 1
        assert hero_test._book['Lightning'][0] == 1
        assert hero_test._life[0] == 50
        
    def test_lvl_up(self, hero_test):
        hero_test.lvl_up()
        assert hero_test.lvl == 2
        
    def test_add_xp(self, hero_test, monster_test):
        hero_test.add_xp(monster_test) 
        assert hero_test.lvl == 2
        assert hero_test.xp == 75
        assert hero_test.xp_lvl_up == 120

    def test_turn(self, hero_test, monster_test):
        hero_test.turn(monster_test, 1)
        assert monster_test._life == (36, 40)
        hero_test.turn(monster_test, 2)
        assert hero_test._life == (50, 50)
        hero_test.turn(monster_test, 3)
        assert monster_test._life == (31, 40)
        hero_test.turn(monster_test, 4)
        assert monster_test._life == (25, 40)
        hero_test.turn(monster_test, 5)
        assert monster_test._life == (20, 40)
        hero_test.turn(monster_test, 5)