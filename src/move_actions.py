from pokemon import Pokemon
from move import Move

def other_damage(move:Move,this:Pokemon,other:Pokemon):
    other.recive_damage(this,move)

def low_this_atk(move:Move,this:Pokemon,other:Pokemon):
    pass