import pytest
from Monster import Monster

@pytest.fixture
def monster_test():
    return Monster("Gobelin","Warrior",27)

class TestMonster():
    def var_test(self, monster_test):
        assert monster_test.name == "Gobelin"
        assert monster_test.rank == "Warrior"
        assert monster_test.xp == 27
        
    def test_tour(self):
        pass