from pokemon import *
import move_actions as move_actions
moves=[Move("xd","GRASS",100,"PHISICAL")]



s = Stats((40,80,100,30,30,20))

p1 = Pokemon("p1",10,s,moves,["ROCK"])
p2 = Pokemon("p2",10,s,moves,["WATER"])

print(p2.stats.hp)

p1.moves[0].attack=move_actions.other_damage
p1.moves[0].attack(p1.moves[0],p1,p2)

print(p2.stats.hp)