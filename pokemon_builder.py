#%%
import json
import numpy
import os

location = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(location, 'pokemon_data.txt'))
pokemons, moves = json.loads(f.read())
f.close()

def make(level, pokemon_id = None):
    if pokemon_id == None:
        idx = numpy.random.randint(0, len(pokemons))
    else:
        idx = pokemon_id - 1

    generated = {}

    pokemon = pokemons[idx]
    generated['level'] = level
    generated['hp'] = ((pokemon['hp'] + 8) * 2 * level) / 100.0 + level + 10
    for stat in ['attack', 'defense', 'speed', 'sp_atk', 'sp_def']:
        generated[stat] = ((pokemon[stat] + 8) * 2 * level) / 100.0 + 5

    potential_moves = []
    for move in pokemon['moves']:
        if move['name'] in moves and moves[move['name']]['power'] > 0 and move['learn_type'] == 'level up' and level >= move['level']:
            potential_moves.append((move['level'], moves[move['name']]))

    generated['moves'] = []
    for level, move in sorted(potential_moves, key = lambda x : x[0], reverse = True)[0:4]:
        generated['moves'].append({
            'power' : move['power'],
            'pp' : move['pp'],
            'type' : str(move['type']).lower(),
            'name' : str(move['name']).lower(),
            'accuracy' : move['accuracy'],
            'id' : move['id']
        })

    generated['name'] = pokemon['name'].lower()
    generated['id'] = idx + 1
    generated['type'] = set([t['name'] for t in pokemon['types']])
    return generated
#%%

#pokemon = make(50)
#print pokemon['name'], ':', pokemon['type']
#for move in pokemon['moves']:
#    print move['name'], move['power']
