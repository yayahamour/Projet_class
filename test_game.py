import pytest
from game import Game
import mock
import builtins

@pytest.fixture
def game_test():
    return Game()

def test_game_start(game_test):
   with mock.patch.object(builtins, 'input', lambda _: '1'):
       game_test.start()

def test_next_stage(game_test, capsys):
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