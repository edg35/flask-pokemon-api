import json
import math
import random

from bson import json_util
from flask import Flask, make_response, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.pokemon
pokedex = db.pokedex

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(request):
    return render_template('404.html')

@app.route('/api/v1/getsinglerandompokemon', methods=['GET'])
def getsinglerandompokemon():
    #generate random pokemon index
    pokemon_index = random.randint(0,1010)
    
    #query mongo database and return pokemon
    pokemon = pokedex.find({'index': pokemon_index})
    return json.loads(json_util.dumps(pokemon))

@app.route('/api/v1/getlistrandompokemon/<int:n>', methods=['GET'])
def getlistrandompokemon(n):
    #make a list of id values for each pokemon in database
    input = range(0,1011)
    
    #make array of random unique values
    ids = random.sample(input, n)
    
    #query mongo database and return data
    pokemon = pokedex.find({'index': {'$in': ids}})
    return json.loads(json_util.dumps(pokemon))
    
@app.route('/api/v1/getpokemonbyid/<int:id>', methods=['GET'])
def getpokemonbyid(id):
    #check to see if id is valid, return error if not
    if id > 1010:
        res =  make_response('Error: Invalid identifier')
        res.status_code = 404
        return res
    
    #else return requested pokemon
    pokemon = pokedex.find({'index': id})
    return json.loads(json_util.dumps(pokemon))

@app.route('/api/v1/getpokemonbyname/<string:name>', methods=['GET'])
def getpokemonbyname(name):
    #check to see if name is valid, return error if not
    if len(name) == 0:
        res = make_response('Error: Invalid name')
        res.status_code = 404
        return res
    
    #else format the name since mongo is case sensitive
    formatted_name = name.capitalize()
    
    #query the database for name and set up response
    pokemon = pokedex.find({'name': formatted_name})
    pokemon = json.loads(json_util.dumps(pokemon))
    
    #check if name exists in database, return error if not
    return pokemon if len(pokemon) > 0 else make_response('Error: Invalid name')

@app.route('/api/v1/getpokemonbyregion/<string:region>', methods=['GET'])
def getpokemonbyregion(region):
    #check to see if reqion is valid, return error
    regions = ["kanto", "sinnoh", "unova", "kalos", "paldea", "joto"]
    formatted_string = region.lower()
    
    if formatted_string not in regions:
        error_response = make_response('Error: Invalid region')
        error_response.status = 404
        return error_response
    
    formatted_string += "_number"
    
    pokemon = pokedex.find({formatted_string: {"$type": "int"}})
    return json.loads(json_util.dumps(pokemon))

@app.route('/handleformsubmit', methods=['POST'])
def handleformsubmit():
    #TODO: handle response from form and present it to developer
    if request.method == 'POST':
        form = request.form
        print(form)
        return render_template("index.html")
     
    if request.method == 'GET':
        res = make_response('Get request not allowed')
        res.status = 404
        return res
         
if __name__ == '__main__':
    app.run(debug=True)
    