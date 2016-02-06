import pokemon_builder as pb
import battle
a =None;
b = None;
def runTest():
	global a
	global b
	a = pb.make(50)
	b = pb.make(50)

	c = battle.attack(a,a["moves"][1],b)
	d = battle.EAttack(a,a["moves"][1],b)
	print(a["name"]," attacked ",b["name"]," with ", a["moves"][1]["name"], " for ",c, " damage. We expected ",d," damage." )

	ct =0
	for i in range(1000):
		ct += battle.attack(a,a["moves"][1],b)/1000

	print(a["name"]," attacked ",b["name"]," with ", a["moves"][1]["name"], " for average",ct, " damage. We expected ",d," damage." )

runTest()