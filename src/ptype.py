types = {"NORMAL", "FIRE","WATER","GRASS","FLYING","FIGHTING", "POISON", "ELECTRIC", "GROUND", "ROCK", "PSYCHIC", "ICE", "BUG", "GHOST", "STEEL","DRAGON","DARK","FAIRY"}


def calc_efectivity(t1:str,t2:str) -> float: #efectividad de t1 sobre t2
    '''Calcula la efectividad de t1 sobre el t2
    puede devolver 0,0.5,1,2
    '''
    e:float 
    
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
            