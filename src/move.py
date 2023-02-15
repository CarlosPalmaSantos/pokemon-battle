from pokemon import Pokemon
def parse_action(s:str):
    if s == "other_damage":
        return other_damage
    if s == "low_this_atk":
        return other_damage


class Move:
    name:str
    description:str
    ptype:str
    power:int
    mtype:str
    user:Pokemon
    attack=None
    
    def __init__(self,name:str,ptype:str,power:int,mtype:str,attack:str) -> None:
        self.name=name
        self.ptype=ptype
        self.power=power
        self.mtype=mtype
        self.attack = parse_action(attack)
        
    def make_attack(self,target:Pokemon):
        other_damage(self,self.user,target)
        
def other_damage(move:Move,this,other):
    return other.recive_damage(other,move)

def low_this_atk(move:Move,this,other):
    pass
