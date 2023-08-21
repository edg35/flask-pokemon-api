import json
import math
import random

from bson import json_util
from flask import Flask, make_response, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.pokemon
pokedex = db.pokedex

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

#TODO: implement api endpoint to get multiple random pokemon
#TODO: implement api endpoint to get pokemon by region
#TODO: implement api endpoint to redirect user to pokemon info screen
#TODO: implement api  ednpoint to handle 404 errors

@app.route('/api/v1/getsinglerandompokemon', methods=['GET'])
def getsinglerandompokemon():
    pokemon_index = random.randint(0,1010)
    pokemon = pokedex.find({'index': pokemon_index})
    return json.loads(json_util.dumps(pokemon))

@app.route('/api/v1/getpokemonbyid/<int:id>', methods=['GET'])
def getpokemonbyid(id):
    if id > 1010:
        res =  make_response('Error: Invalid identifier')
        res.status_code = 404
        return res
    
    pokemon = pokedex.find({'index': id})
    return json.loads(json_util.dumps(pokemon))

@app.route('/api/v1/getpokemonbyname/<string:name>', methods=['GET'])
def getpokemonbyname(name):
    if len(name) == 0:
        res = make_response('Error: Invalid name')
        res.status_code = 404
        return res
    
    formatted_name = name.capitalize()
    pokemon = pokedex.find({'name': formatted_name})
    pokemon = json.loads(json_util.dumps(pokemon))
    return pokemon if len(pokemon) > 0 else make_response('Error: Invalid name')

if __name__ == '__main__':
    app.run(debug=True)
    