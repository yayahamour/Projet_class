import pytest
from Monster import Monster
from Hero import Hero

hero_dict_test = {"Heal":(2,3,10), "Fire":(0,1,5), "Ice":(1,1,6), "Lightning":(0,1,5)}
monster_dict_test = {"Heal":(2,3,10), "Fire":(0,0,5), "Ice":(0,0,6), "Lightning":(0,0,5)}

@pytest.fixture
def monster_test():
    return Monster((40, 40), 10, monster_dict_test, "Gobelin", "Warrior", 75)

@pytest.fixture
def hero_test():
    return Hero((50, 50), 10, hero_dict_test, 0, 1, 50)
class TestMonster():
    def var_test(self, monster_test):
        assert monster_test.name == "Gobelin"
        assert monster_test.rank == "Warrior"
        assert monster_test.xp == 27
        
    def test_tour(self, monster_test, hero_test):
        pass