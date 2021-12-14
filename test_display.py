import pytest
from display import Display
from hero import Hero

HERO_DICT_SAMPLE = {"Heal":(2,3,10), "Fire":(0,1,5), "Ice":(0,1,6), "Lightning":(1,1,5)}

@pytest.fixture
def hero_test():
    return Hero((45,50), 5, 1, 5, HERO_DICT_SAMPLE, 0, 1, 50)
def display_test():
    return Display()

class TestDisplay:
    
    def test_display_stats(self, hero_test):
        pass