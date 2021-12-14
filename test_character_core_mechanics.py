import pytest
from character_core_mechanics import CharacterCoreMechanics

@pytest.fixture
def character():
    return (CharacterCoreMechanics((10,15), 6, 1, 5, {"Heal":(3,4,10), "Fire":(1,5,5), "Ice":(1,4,5), "Lightning":(1,5,5)}))
    
@pytest.fixture
def character_():
    return (CharacterCoreMechanics((50,70), 5, 1, 5, {"Heal":(1,10,5), "Fire":(0,5,-5), "Ice": (0,5,5), "Lightning":(0,5,5)}))

@pytest.fixture
def test():
    return (CharacterCoreMechanics((4,70), 5, 1, 5, {"Heal":(1,10,5), "Fire":(0,5,-5), "Ice": (0,5,5), "Lightning":(0,5,5)}))
class TestCharacterCoreMechanics():
    
    def test_core_var(self, character):
        assert character._life == (10,15)
        assert character._crit_rate == 5
        assert character._strength == 6
        assert character._armor == 1
        assert character._book == {"Heal":(3,4,10), "Fire":(1,5,5), "Ice":(1,4,5), "Lightning":(1,5,5)}
        
    def test_base_attack(self, character, character_, test):
        character.base_attack(character_)
        assert character_._life[0] == 45 or character_._life[0] == 39
        character.base_attack(test)
        assert test._life[0] == 0

    def test_use_spell(self, character, character_):
        character.use_spell("Fire", character_)
        assert character_._life[0] == 45
        assert character._book["Fire"][0] == 0
        character.use_spell("Ice", character_)
        assert character_._life[0] == 40
        assert character._book["Ice"][0] == 0
        character.use_spell("Lightning", character_)
        assert character_._life[0] == 35 or character_._life[0] == 30
        assert character._book["Lightning"][0] == 0
        character.use_spell("Heal")
        assert character._life[0] == 15
        character_.use_spell("Heal")
        assert character_._life[0] == 40 or character_._life[0] == 45

    