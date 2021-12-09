from dataclasses import dataclass, field
from typing import ClassVar
from character_core_mechanics import CharacterCoreMechanics

@dataclass
class Hero(CharacterCoreMechanics):
    xp: int = 0
    lvl: int = 1
    xp_lvl_up: int =50
    
    def camp(self):
        
        #Replace spellbook with Hero.book
        
        spell_max = self._book['Heal'][1]
        power = self._book['Heal'][2]
        self._book['Heal'] = (spell_max, spell_max, power)

        spell_max = self._book['Fire'][1]
        power = self._book['Fire'][2]
        self._book['Fire'] = (spell_max, spell_max, power)

        spell_max = self._book['Ice'][1]
        power = self._book['Ice'][2]
        self._book['Ice'] = (spell_max, spell_max, power)

        spell_max = self._book['Lightning'][1]
        power = self._book['Lightning'][2]
        self._book['Lightning'] = (spell_max, spell_max, power)
        
        if self._life[0] < self._life[1]:
            life_max = self._life[1]
            self._life = (self._life[0] + 10, life_max)
            if self._life[0] > self._life[1]:
                self._life = (life_max, life_max)
    
    def lvl_up(self) -> dict:
        self.lvl += 1
        if self.lvl == 5:
            pass
        
    def add_xp(self, monster) -> int:
        self.xp += monster.xp
        if self.xp >= self.xp_lvl_up:
            self.lvl_up()
            self.xp_lvl_up += 50 + (self.lvl * 10)
        return self.xp
    
    def tour(self, target) -> list:
        return None