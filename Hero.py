from dataclasses import dataclass
from character_core_mechanics import CharacterCoreMechanics

import os
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
    
    def cible(self, monsters):
        cnt = 1
        n = 0
        while (n != 5):
            for monster in monsters:
                print(f" Enemie {cnt} : {monster._life} pv")
                cnt+=1
            cible = int(input("Quel enemie voulez-vous cibler : "))
            if(isinstance(int, cible)):
                if (cible > cnt or cible < 0):
                    print("Entrer valeur correct")
                    n += 1
                elif(cible < cnt):
                    return cible
            else:
                os.system("cls")
                n += 1
        return False

    def turn(self, _input, monsters) -> list:
        if(_input != 2):
            target = self.cible(monsters)
            if(isinstance(bool,target)):
                return False
        if _input == 1:
            self.base_attack(target)
            
        elif _input == 2:
            if self._book['Heal'][0] > 0:
                self.use_spell('Heal')
            else:
                return False
            
        elif _input == 3:
            if self._book['Fire'][0] > 0:
                self.use_spell('Fire', target)
            else:
                return False
            
        elif _input == 4:
            if self._book['Ice'][0] > 0:
                self.use_spell('Ice', target)
            else:
                return False
            
        elif _input == 5:
            if self._book['Lightning'][0] > 0:
                self.use_spell('Lightning', target)
            else:
                return False
