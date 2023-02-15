from move import Move

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
        moves
        self.types=types
        
        for m in moves:
            m.user=self
            self.moves.append(m)
    
    def recive_damage(self,other,move:Move):
        B:bool = True#stab a favor
        
        ef = [calc_efectivity(move.ptype,t) for t in self.types if t != None]
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
        return f"{self.name}: {move.name}-> {other.name} {{{move.ptype}->{self.types}:{E}}}"
    
types = {"NORMAL", "FIRE","WATER","GRASS","FLYING","FIGHTING", "POISON", "ELECTRIC", "GROUND", "ROCK", "PSYCHIC", "ICE", "BUG", "GHOST", "STEEL","DRAGON","DARK","FAIRY"}

def calc_efectivity(t1:str,t2:str) -> float: #efectividad de t1 sobre t2
    '''Calcula la efectividad de t1 sobre el t2
    puede devolver 0,0.5,1,2
    '''
    e:float 
    
    print(f"{t1}->{t2}")
    
    if t1 == "FIRE":
        if t2 == "FIRE" or t2 == "WATER" or t2 == "ROCK" or t2 == "DRAGON":
            e = 0.5
        elif t2 == "GRASS" or t2 == "ICE" or t2 == "BUG" or t2 == "STEEL":
            e = 2
        
    elif t1 == "WATER":
        if t2 == "WATER" or t2 == "GRASS" or t2 == "DRAGON":
            e = .5
        elif t2 == "FIRE" or t2 == "GROUND" or t2 == "ROCK":
            e = 2
            
    else:
        e = 1
        
    return e
            