from pokemon import Pokemon,Stats
from move import Move
moves=[Move("xd","WATER",100,"PHISICAL","other_damage")]



s = Stats((40,80,100,30,30,20))

p1 = Pokemon("p1",10,s,moves,["WATER"])
p2 = Pokemon("p2",10,s,moves,["FIRE"])

print(p2.stats.hp)
print(p1.moves[0].make_attack(p2))

print(p2.stats.hp)