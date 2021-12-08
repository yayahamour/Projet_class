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
        
        if spellbook['Heal'][0] < 3:
            power = spellbook['Heal'][1]
            spellbook['Heal'] = (3, power)
            
        if spellbook['Fire'][0] < 1:
            power = spellbook['Fire'][1]
            spellbook['Fire'] = (1, power)
            
        if spellbook['Ice'][0] < spellbook['Ice'][1]:
            power = spellbook['Ice'][1]
            spellbook['Ice'] = (1, power)
            
        if spellbook['Lightning'][0] < spellbook['Lightning'][1]:
            spell_max = spellbook['Lightning'][1]
            power = spellbook['Lightning'][2]
            spellbook['Lightning'] = (1, spell_max, power)
        
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
        # monster.xp
        self.xp += monster
        if self.xp >= self.xp_lvl_up:
            self.lvl_up()
            self.xp_lvl_up += 50 + (self.lvl * 10)
        return self.xp
    
    def tour(self, target) -> list:
        pass