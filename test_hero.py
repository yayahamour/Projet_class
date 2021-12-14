from sys import path
path.append("./src")
import pytest
from hero import Hero
import mock
import builtins
from monster import Monster

HERO_DICT_SAMPLE = {"Heal":(2,3,10), "Fire":(1,1,5), "Ice":(1,1,6), "Lightning":(1,1,5)}
MONSTER_DICT_SAMPLE  = {"Heal":(2,3,10), "Fire":(0,0,5), "Ice":(0,0,6), "Lightning":(0,0,5)}



@pytest.fixture
def hero_test():
    return Hero((45,50), 5, 1, 5, HERO_DICT_SAMPLE, 0, 1, 50)

@pytest.fixture
def monster_test():
    liste = []
    liste.append(Monster((40, 40), 10, 1, 5, MONSTER_DICT_SAMPLE, "Gobelin", 75))
    return liste
class TestHero():
         
    def test_hero_var(self, hero_test):
        assert hero_test._life == (45,50)
        assert hero_test._strength == 5
        assert hero_test._crit_rate == 5
        assert hero_test._armor == 1
        assert hero_test._book == HERO_DICT_SAMPLE
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
        
    def test_attack_turn(self, hero_test, monster_test, capsys):
        with mock.patch.object(builtins, 'input', lambda _: 'dqsdf'):
            assert hero_test.turn(1, monster_test) == False
        with mock.patch.object(builtins, 'input', lambda _: '9'):
            assert hero_test.turn(1, monster_test) == False
        with mock.patch.object(builtins, 'input', lambda _: '-1'):
            assert hero_test.turn(1, monster_test) == False
        with mock.patch.object(builtins, 'input', lambda _: '1'):
            hero_test.turn(1, monster_test)
            assert monster_test[0]._life[0] == 36 or monster_test[0]._life[0] == 31
        
    def test_heal_turn(self, hero_test, monster_test):
        hero_test.turn(2, monster_test)
        assert hero_test._life[0] == 50
        
    def test_fire_turn(self, hero_test, monster_test): 
        with mock.patch.object(builtins, 'input', lambda _: '1'):
            hero_test.turn(3, monster_test)
            assert monster_test[0]._life[0] <= 34 or monster_test[0]._life[0] >= 30
        
    def test_ice_turn(self, hero_test, monster_test): 
        with mock.patch.object(builtins, 'input', lambda _: '1'):
            hero_test.turn(4, monster_test)
            assert monster_test[0]._life[0] <= 34 and monster_test[0]._life[0] >= 28
        
    def test_lightning_turn(self, hero_test, monster_test): 
        with mock.patch.object(builtins, 'input', lambda _: '1'):
            hero_test.turn(5, monster_test)
            assert monster_test[0]._life[0] >= 29 and monster_test[0]._life[0] <= 36

    def test_lvl_up(self, hero_test):
            for i in range(0, 8):
                hero_test.lvl_up()
            assert hero_test.lvl == 9
            assert hero_test._book['Heal'][0] == 2
            assert hero_test._book['Fire'][0] == 5
            assert hero_test._book['Ice'][0] == 4
            assert hero_test._book['Lightning'][0] == 3
            
    def test_add_xp(self, hero_test, monster_test):
        hero_test.add_xp(monster_test[0]) 
        assert hero_test.lvl == 2
        assert hero_test.xp == 75
        assert hero_test.xp_lvl_up == 120