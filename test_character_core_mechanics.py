from typing import Type
import pytest
from character_core_mechanics import CharacterCoreMechanics

class TestCharacterCoreMechanics():
    @pytest.fixture
    def character():
        return (CharacterCoreMechanics((10,15), 5, {"Heal":(3,4,10), "Fire":(1,5,5), "Ice":(1,4,5), "Lightning":(1,5,5)}))
    
    @pytest.fixture
    def character_():
        return (CharacterCoreMechanics((50,70), -50, {"Heal":(1,10,5), "Fire":(0,5,-5), "Ice": (0,5,5), "Lightning":(0,5,5)}))

    def test ():
        return(CharacterCoreMechanics(("-1",""), "", {"Heal":("",10,5), "Fire":(-1,5,5), "Ice": (0,-5,5), "Lightning":(0,5,5)}))

    
    def test_base_attack(character, character_, test):
        assert character.base_attack(character_) == character_._life[0] - 5

        with pytest.raises(ValueError):
            character_.base_attack(character)
                
        with pytest.raises(TypeError):
            character.base_attack("")
            character.base_attack(test)
            test.base_attack(character)

    
    def test_use_spell(character, character_, test):
        test1 = CharacterCoreMechanics(5, "", {"Heal":("",10,5), "Fire":(-1,5,5), "Ice": (0,-5,5), "Lightning":(0,5,5)})
        test2 = CharacterCoreMechanics((-25, 58)), "", {"Heal":("",10,5), "Fire":(-1,5,5), "Ice": (0,-5,5), "Lightning":(0,5,5)})

        with pytest.raises(TypeError):
            character.use_spell(1, character_)
            character.use_spell("Fire", "er")
            character.use_spell("Heal", character)
            character.use_spell("Fire", test1)

        with pytest.raises(ValueError("Vous n'avez pas accée à ce spell")):
            character.use_spell("Fire", character)

        with pytest.raises(ValueError):
            test.use_spell("Fire", character)
            test.use_spell("Ice", character)
            character.use_spell("Fire", test2)

        with pytest.raises(KeyError):
            character.use_spell("az", character_)
        
       

        assert character.use_spell("Fire", character_) == 45
        assert character.book["Fire"][0] == 0
        assert character.use_spell("Ice", character_) == 45
        assert character.book["Ice"][0] == 0
        assert character.use_spell("Lightning", character_) == 45
        assert character.book["Lightning"][0] == 0
        character.test_use_spell("Heal")
        assert character._life == 15
        character_.test_use_spell("Heal")
        assert character._life == 60

    