from dataclasses import dataclass, field
from typing import ClassVar
from character_core_mechanics import CharacterCoreMechanics
import random


@dataclass
class Monster(CharacterCoreMechanics):
    rank: str
    xp: int
    
    def turn(self, hero):
        
        if self.rank == 'Gobelin':
            self.base_attack(hero)
            
        if self.rank == 'Liche':
            r_num = random.randint(1,100)
            if r_num <= 60:
                self.base_attack(hero)
            else:
                self.use_spell('Fire', hero)
                
        if self.rank == 'Boss':
            self.base_attack(hero)
            self.base_attack(hero)