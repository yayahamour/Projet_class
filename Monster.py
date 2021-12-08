from dataclasses import dataclass, field
from typing import ClassVar
# from CharacterCoreMechanics import CharacterCoreMechanics

@dataclass
class Monster():
    name: str
    rank: str
    xp: int
    
    def tour(self, hero):
        if self.rank == 'Gobelin':
            pass
        if self.rank == 'Liche':
            pass
        if self.rank == 'Boss':
            pass
        return None