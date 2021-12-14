import pytest

from game import Game

@pytest.fixture
def game_test():
    return Game()

# def test(self, game_test):
#     with()