#%%

import urllib2
import json
import os

location = os.path.dirname(os.path.abspath(__file__))

pokemons = []

for i in range(1, 152):
    response = urllib2.urlopen('http://pokeapi.co/api/v1/pokemon/{0}/'.format(i))

    pokemons.append(json.load(response))

    print i

base = 'http://pokeapi.co'

moves = {}
for i in range(1, 166):
    response = urllib2.urlopen('http://pokeapi.co/api/v1/move/{0}/'.format(i))

    move = json.load(response)

    moves[move['name']] = move

    print i

f = open(os.path.join(location, 'pokemon_data.txt'), 'w')
f.write(json.dumps([pokemons, moves]))
f.close()
#%%
