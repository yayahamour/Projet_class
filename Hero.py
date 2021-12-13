from dataclasses import dataclass, field
from typing import ClassVar
from character_core_mechanics import CharacterCoreMechanics
from menu import Menu

@dataclass
class Hero(CharacterCoreMechanics):
    xp: int
    lvl: int
    xp_lvl_up: int
    
    def camp(self) -> dict:
        
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
        max_life = self._life[1]
        current_life = self._life[0]
        self._life = (current_life, max_life + 5)
        self._strength += 1
        self._crit_rate += 1
        
        if self.lvl == 2:
            max_use = self._book['Fire'][1] + 1
            self._book['Fire'] = (max_use, max_use, 6)
            
        if self.lvl == 4:
            max_use = self._book['Fire'][1] + 1
            self._book['Fire'] = (max_use, max_use, 6)
            
            max_use = self._book['Ice'][1] + 1
            self._book['Ice'] = (max_use, max_use, 8)   
              
        if self.lvl == 6:
            max_use = self._book['Fire'][1] + 1
            self._book['Fire'] = (max_use, max_use, 8)
            
            max_use = self._book['Ice'][1] + 1
            self._book['Ice'] = (max_use, max_use, 9) 
              
            max_use = self._book['Lightning'][1] + 1
            self._book['Lightning'] = (max_use, max_use, 12)   
            
        if self.lvl == 8:
            self._strength += 4
            self._crit_rate += 10
            
            max_use = self._book['Fire'][1] + 1
            self._book['Fire'] = (max_use, max_use, 12)
            
            max_use = self._book['Ice'][1] + 1
            self._book['Ice'] = (max_use, max_use, 15) 
              
            max_use = self._book['Lightning'][1] + 1
            self._book['Lightning'] = (max_use, max_use, 18) 
            
            max_life = self._life[1]
            current_life = self._life[0]
            self._life = (current_life, max_life + 15)
            
    def add_xp(self, monster) -> int:
        self.xp += monster.xp
        if self.xp >= self.xp_lvl_up:
            self.lvl_up()
            self.xp_lvl_up += 50 + (self.lvl * 10)
    
    def turn(self, target, input) -> list:

        if input == 1:
            self.base_attack(target)
            
        elif input == 2:
            if self._book['Heal'][0] > 0:
                self.use_spell('Heal', target)
            else:
                return False
            
        elif input == 3:
            if self._book['Fire'][0] > 0:
                self.use_spell('Fire', target)
            else:
                return False
            
        elif input == 4:
            if self._book['Ice'][0] > 0:
                self.use_spell('Ice', target)
            else:
                return False
            
        elif input == 5:
            if self._book['Lightning'][0] > 0:
                self.use_spell('Lightning', target)
            else:
                return False
        else:
            return False
        
        return True