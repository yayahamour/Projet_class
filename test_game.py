from sys import path
path.append("./src")
import pytest
import mock
import builtins
from display import Display
from game import Game
from hero import Hero
from monster import Monster

@pytest.fixture
def game_test():
    return Game()

HERO_DICT_SAMPLE = {"Heal":(2,3,10), "Fire":(0,1,5), "Ice":(0,1,6), "Lightning":(1,1,5)}

monsters = [Monster((40, 40), 4, 1, 5, {}, "Gobelin", 75),Monster((40, 40), 4, 1, 5, {}, "Gobelin", 75)]

@pytest.fixture
def game_test():
    return Game(Hero((45,50), 5, 1, 5, HERO_DICT_SAMPLE, 0, 1, 50), Display(), monsters, stage=1)

class TestGame:
    def test_game_start(self, game_test):
        with mock.patch.object(builtins, 'input', lambda _: '1'):
            game_test.start()

    def test_next_stage(self, game_test, capsys):
        game_test.stage = 5
        strout = ["Vous montez longuement un escalier en collimasson pour arriver à l'étage 6\n",
              "Vous étes en lieu sur, profitez en pour vous reposer\n"]
        game_test.next_stage()
        assert capsys.readouterr().out == "".join(strout)
        assert game_test.player._armor == 0 or game_test.player._armor == 1
        game_test.monsters = []
        game_test.stage = 6
        game_test.next_stage()
        assert len(game_test.monsters) == 2
        game_test.monsters = []
        game_test.stage = 12
        game_test.next_stage()
        assert len(game_test.monsters) == 3

    def test_next_stage_drake(game_test, capsys):
        game_test.stage = 9
        strout = ["Vous montez longuement un escalier en collimasson pour arriver à l'étage 10\n",
                "U..UUUNN... UUUUNNNN DRAAAAAAGGGGOONNNN FUUUUYYYEEZZZ\n"]
        game_test.next_stage()
        assert capsys.readouterr().out == "".join(strout)

    def test_next_stage_orc(game_test, capsys):
        game_test.stage = 4
        strout = ["Vous montez longuement un escalier en collimasson pour arriver à l'étage 5\n",
                "Un Orc se dresse devant vous, je vous avez prévenu\n"]
        game_test.next_stage()
        assert capsys.readouterr().out == "".join(strout)
    
    def test_save(self, game_test):
        assert game_test.save() == True
        
    def test_load(self, game_test, save_name = 'jean'):
        hero, stage, monsters = game_test.load(save_name)
        game = Game(hero, Display(), monsters, stage)
        assert game.player == game_test.player
        assert game.stage == game_test.stage
        assert game.monsters == game_test.monsters
        
    def test_delete_save(self, game_test, save_name = 'jean'):
        assert game_test.delete_save(save_name) == True
