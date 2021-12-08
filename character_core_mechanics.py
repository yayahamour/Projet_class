from dataclasses import dataclass, field

from _pytest.python_api import raises

@dataclass
class CharacterCoreMechanics():
    _life : tuple
    _strenght : int
    _book : dict = field(default_factory=dict)

    def base_attack(self, target):
        if (type(self._strenght) == int and type(target._life[0]) == int and type(self._strenght) == int):
            if(self._strenght > 0):
                vie = target._life[0] - self._strenght
                target._life = (vie, target._life[1])
                return target
            else:
                raises(ValueError)
        else:
            raise(TypeError)

    def use_spell(self, spell, target=None):
        if(spell == "Heal"):
            life = (self._life[0]+self._book[spell][2])
            if (life > self._life[1]):
                life = self._life[1]
            self._life = (life, self._life[1])
            self._book[spell] = (self._book[spell][0] - 1, self._book[spell][1], self._book[spell][2])
        else:
            life = target._life[0] - self._book[spell][2]
            target._life = (life, target._life[1])
            self._book[spell] = (self._book[spell][0] - 1, self._book[spell][1], self._book[spell][2])   