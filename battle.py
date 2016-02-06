
import random
#maps the type strings to the indexes
typeMap ={
'normal':0,
'fire':1,
'water':2,
'electric':3,
'grass':4,
'ice':5,
'fighting':6,
'poision':7,
'ground':8,
'flying':9,
'psychic':10,
'bug':11,
'rock':12,
'ghost':13,
'dragon':14
}

#maps type strings to physical or special
moveType ={
'normal':0,
'fire':1,
'water':1,
'electric':1,
'grass':1,
'ice':1,
'fighting':0,
'poision':0,
'ground':0,
'flying':0,
'psychic':1,
'bug':0,
'rock':0,
'ghost':0,
'dragon':2
}



effectTable = [
[1,1,1,1,1,1,1,1,1,1,1,1,0.5,0,1],
[1,0.5,0.5,1,2,2,1,1,1,1,1,2,0.5,1,0.5],
[1,2,0.5,1,0.5,1,1,1,2,1,1,1,2,1,0.5],
[1,1,2,0.5,0.5,1,1,1,0,2,1,1,1,1,0.5],
[1,0.5,2,1,0.5,1,1,0.5,2,0.5,1,0.5,2,1,0.5],
[1,1,0.5,1,2,0.5,1,1,2,2,1,1,1,1,2],
[2,1,1,1,1,2,1,0.5,1,0.5,0.5,0.5,2,0,1],
[1,1,1,1,2,1,1,0.5,0.5,1,1,2,0.5,0.5,1],
[1,2,1,2,0.5,1,1,2,1,0,1,0.5,2,1,1],
[1,1,1,0.5,2,1,2,1,1,1,1,2,0.5,1,1],
[1,1,1,1,1,1,2,2,1,1,0.5,1,1,1,1],
[1,0.5,1,1,2,1,0.5,2,1,0.5,2,1,1,1,1],
[1,2,1,1,1,2,0.5,1,0.5,2,1,2,1,1,1],
[0,1,1,1,1,1,1,1,1,1,0,1,1,2,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
]


def getAtkName(mType):
	"attack" if (moveType[mType] ==0) else "sp_atk"

def getDefName(mType):
	"defense" if (moveType[mType] ==0) else "sp_def"

def getEffect(atkType, defType):
	return effectTable[typeMap[atkType]][typeMap[defType]]


def damageEq(atkLevel, atkStat, atkBase, defStat, STAB, effect):
	return lambda x: ((((2*atkLevel)/5+2)*atkStat*atkBase)/(defStat*50)+2)*STAB*effect*x

def damage(atkLevel, atkStat, atkBase, defStat, STAB, effect):
	return damageEq(atkLevel, atkStat, atkBase, defStat, STAB, effect)(random.uniform(.85,1))

def EDamage(atkLevel, atkStat, atkBase, defStat, STAB, effect):
	return damageEq(atkLevel, atkStat, atkBase, defStat, STAB, effect)(0.925)

def isCritical(speed,highCrit):
	2 if(speed*100/ (64 if highCrit else 512) < random.random()) else 1

#yeilds the damage done by an attacker performing a move on a defender
def attack(attacker, move, defender):
	atkStat = attacker[getAtkName(move["type"])]
	defStat = defender[getDefName(move["type"])]
	atkLevel = attacker["level"]
	atkBase = move["power"]
	STAB = 1.5 if(move["type"] in attacker["type"]) else 1
	effect = reduce((lambda x,y: x*getEffect(move["type"],y)), defender["type"], 1)
	crit = isCritical(attacker["speed"], 0)
	return damage(atkLevel*crit, atkStat, atkBase, defStat, STAB, effect)


