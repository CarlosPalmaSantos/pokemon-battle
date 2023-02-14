from move import *
from ptype import *
import random
class Stats:
    hp:int 
    atk:int
    df:int
    spa:int
    spd:int
    spe:int

    def __init__(self,stats:tuple[int]) -> None:
        self.hp = stats[0]
        self.atk = stats[1]
        self.df = stats[2]
        self.spa = stats[3]
        self.spd = stats[4]
        self.spe = stats[5]
        

class Pokemon:
    name:str
    level:int
    stats:Stats
    moves:list[Move]
    types:list[str]
    
    def __init__(self,name:str,level:int, stats:Stats,moves:list[Move],types:list[str]) -> None:
        self.name=name
        self.level=level
        self.stats=stats
        self.moves=moves
        self.types=types
        
    
    def recive_damage(self,other,move:Move):
        B:bool = True#stab a favor
        
        ef = [calc_efectivity(move.ptype,t) for t in types if t != None]
        E:float = 1
        for e in ef:
            E*=e
        
        V:int = random.randint(85,100)
        dam_2:float = 0
        if move.mtype == "PHISICAL":
            dam_2 = ((0.2*self.level+1)*other.stats.atk*move.power/(25*self.stats.df)) + 2  
        elif move.mtype == "SPECIAL":
            dam_2 = ((0.2*self.level+1)*other.stats.spa*move.power/(25*self.stats.spd)) + 2    
        
        dam:float = 0.01*B*E*V*dam_2
        self.stats.hp -= dam
        
    
