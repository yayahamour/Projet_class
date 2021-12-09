from dataclasses import dataclass, field



@dataclass
class CharacterCoreMechanics():
    _life : tuple
    _strenght : int
    _book : dict = field(default_factory=dict)

    def list_spell(self):
        tab = []
        if (self._book["Heal"][0] > 0):
            tab.append("Heal")
        if (self._book["Ice"][0] > 0):
            tab.append("Ice")
        if (self._book["Fire"][0] > 0):
            tab.append("Fire")
        if (self._book["Lightning"][0] > 0):
            tab.append("Lightning")
        return(tab)



    def base_attack(self, target):
        if(self._strenght > 0):
            life = target._life[0] - self._strenght
            if (life < 0):
                life = 0
            target._life = (life, target._life[1])
        return target
        

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