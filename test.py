import pokemon_builder as pb
import battle

a = pb.make(50)
b = pb.make(50)

c = battle.attack(a,a["moves"][1],b)
print(a["name"]," attacked ",b["name"], " for ",c, " damage.")