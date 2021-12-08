import pytest
from Monster import Monster
from Hero import Hero

@pytest.fixture
def monster_test():
    return Monster("Gobelin","Warrior",27)

@pytest.fixture
def hero_test():
    return Hero(0,1,50)
class TestMonster():
    def var_test(self, monster_test):
        assert monster_test.name == "Gobelin"
        assert monster_test.rank == "Warrior"
        assert monster_test.xp == 27
        
    def test_tour(self, monster_test, hero_test):
        assert monster_test.tour(hero_test) == None