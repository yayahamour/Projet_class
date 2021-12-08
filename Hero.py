from dataclasses import dataclass, field
from typing import ClassVar
# from CharacterCoreMechanics import CharacterCoreMechanics

@dataclass
class Hero():
    xp: int
    lvl: int
    xp_lvl_up: int
    
    def camp(self, spellbook, life) -> dict:
        
        #Replace spellbook with Hero.book
        
        spell_max = spellbook['Heal'][1]
        power = spellbook['Heal'][2]
        spellbook['Heal'] = (spell_max, spell_max, power)

        spell_max = spellbook['Fire'][1]
        power = spellbook['Fire'][2]
        spellbook['Fire'] = (spell_max, spell_max, power)

        spell_max = spellbook['Ice'][1]
        power = spellbook['Ice'][2]
        spellbook['Ice'] = (spell_max, spell_max, power)

        spell_max = spellbook['Lightning'][1]
        power = spellbook['Lightning'][2]
        spellbook['Lightning'] = (spell_max, spell_max, power)
        
        if life[0] < life[1]:
            life_max = life[1]
            life = (life[0] + 10, life_max)
            if life[0] > life[1]:
                life = (life_max, life_max)
        
        return spellbook, life
    
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