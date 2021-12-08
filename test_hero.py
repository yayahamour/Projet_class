import pytest
from Hero import Hero
from Monster import Monster

@pytest.fixture
def monster_test():
    return Monster("Gobelin","Warrior",75)

@pytest.fixture
def hero_test():
    return Hero(0,1,50)

@pytest.fixture
def life_test():
    life = (45, 50)
    return life

@pytest.fixture
def spellbook_test():
    dic = {"Heal":(2,3,10), "Fire":(0,1,5), "Ice":(1,1,6), "Lightning":(0,1,5)}
    return dic
class TestHero():
    
    def var_test(self, hero_test):
        assert hero_test.xp == 0
        assert hero_test.lvl == 1
        assert hero_test.xp_lvl_up == 50        
        
    def test_camp(self, hero_test, spellbook_test, life_test):
        spellbook, life = hero_test.camp(spellbook_test, life_test)
        assert spellbook['Heal'][0] == 3 
        assert spellbook['Fire'][0] == 1 
        assert spellbook['Ice'][0] == 1
        assert spellbook['Lightning'][0] == 1
        assert life[0] == 50
        
    def test_lvl_up(self, hero_test):
        hero_test.lvl_up()
        assert hero_test.lvl == 2
        
    def test_add_xp(self, hero_test, monster_test):
        hero_test.add_xp(monster_test) 
        assert hero_test.lvl == 2
        assert hero_test.xp == 75
        assert hero_test.xp_lvl_up == 120
        
    def test_tour(self, hero_test, monster_test):
        assert hero_test.tour(monster_test) == None