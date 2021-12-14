import pytest
from display import Display
from game import Game
from hero import Hero
from monster import Monster

HERO_DICT_SAMPLE = {"Heal":(2,3,10), "Fire":(0,1,5), "Ice":(0,1,6), "Lightning":(1,1,5)}

monsters = [Monster((40, 40), 4, 1, 5, {}, "Gobelin", 75),Monster((40, 40), 4, 1, 5, {}, "Gobelin", 75)]

@pytest.fixture
def game_test():
    return Game(Hero((45,50), 5, 1, 5, HERO_DICT_SAMPLE, 0, 1, 50), Display(), monsters, stage=1)
class TestGame:
    
    def test_save(self, game_test):
        assert game_test.save() == True
        
    def test_load(self, game_test):
        hero, stage, monsters = game_test.load('jean')
        game = Game(hero, Display(), monsters, stage)
        assert game.player == game_test.player
        assert game.stage == game_test.stage
        assert game.monsters == game_test.monsters