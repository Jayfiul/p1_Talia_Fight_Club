import json

import requests
from flask import Flask, request  # web server essentials

from database import database
from database import question
from database import league
from database import anime
from database import pokemon

from routes.home import home_bp
from routes.login import login_bp
from routes.logout import logout_bp
from routes.register import register_bp
from routes.result import result_bp
from routes.test import test_bp
from utils import b64

from utils import lol_api
from utils import poke_api

global db
db = database.Database()


app = Flask(__name__, static_url_path='/static')

app.register_blueprint(home_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(register_bp)
app.register_blueprint(test_bp)
app.register_blueprint(result_bp)

app.secret_key = b64.base64_encode(
    "this is one hell of a secret key. it's really secure now that we encoded it into base64!")

league_characters = lol_api.LOLApi()
poke_api = poke_api.PokeApi()
poke_api.get_all_pokemon()



@app.before_request
def before_request():
    request.db = db

"""
# =======================================================================================================================
# poke API CODE
# =======================================================================================================================

# Helper Function
def color(name):
    pokeAPI = requests.get('https://pokeapi.co/api/v2/pokemon-species/' + str(name))
    pokeInfo = pokeAPI.text  # pulls all the information from the api file and puts in this string variable
    poke_json = json.loads(pokeInfo)
    return poke_json["color"]["name"]


# Helper Function
def shape(name):
    pokeAPI = requests.get('https://pokeapi.co/api/v2/pokemon-species/' + str(name))
    pokeInfo = pokeAPI.text  # pulls all the information from the api file and puts in this string variable
    poke_json = json.loads(pokeInfo)
    return poke_json["shape"]["name"]


# Helper Function
def habitat(name):
    pokeAPI = requests.get('https://pokeapi.co/api/v2/pokemon-species/' + str(name))
    pokeInfo = pokeAPI.text  # pulls all the information from the api file and puts in this string variable
    poke_json = json.loads(pokeInfo)
    return poke_json["habitat"]["name"]


# def types(types):
#    typeAPI = requests.get('https://pokeapi.co/api/v2/type/' + types)
#    typeInfo = typeAPI.text
#    type_json = json.loads(typeInfo)
#    pokemon = []
#    for x in type_json["pokemon"]:
#        pokemon.append(x["pokemon"]["name"])
#    return pokemon
# print(types("dragon"))

# Helper Function
def heavy(weight):
    if weight > 100:
        weight = "heavy"
    else:
        weight = "light"
    return weight


# Helper Function
def types(TYPES):
    types = []
    for x in TYPES:
        types.append(x["type"]["name"])
    return types


# Helper Function
def height(heightER):
    if heightER > 20:
        height = "tall"
    elif heightER > 17:
        height = "medium"
    else:
        height = "short"
    return height


# Help Function that retrieves the image from the API


# MASTER FUNCTION

# PLEASE DO NOT DENIAL-OF-SERVICE THE APIS WE ARE USING!!!!!
def pokemon(name):
    pokeAPI = requests.get('https://pokeapi.co/api/v2/pokemon-species/' + str(name))
    pokeInfo = pokeAPI.text  # pulls all the information from the api file and puts in this string variable
    poke_json = json.loads(pokeInfo)
    id = int(poke_json["id"])

    idAPI = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(id))
    idInfo = idAPI.text
    id_json = json.loads(idInfo)

    pokemon = []

    pokemon.append(poke_json["name"])
    id = int(poke_json["id"])
    pokemon.append(id)

    pokemon.append(poke_json["color"]["name"])
    # pokemon.append(poke_json["shape"]["name"])
    # pokemon.append(poke_json["habitat"]["name"])
    # pokemon.append(poke_json["shape"]["name"])
    if (name == "meltan" or name == "melmetal"):
        pokemon.append("NULL")
    else:
        pokemon.append(poke_json["shape"]["name"])
    pokemon.append(heavy(id_json["weight"]))
    pokemon.append(types(id_json["types"]))
    pokemon.append(height(id_json["height"]))
    pokemon.append(id_json["sprites"]["front_default"])  # tretrieves the image URL

    return pokemon  # returns name, id, color, shape, weight, types, height, image

print(poke_api.get_pokemon("bulbasaur"))
pokeAPI = requests.get('https://pokeapi.co/api/v2/pokemon-species/?offset=0&limit=1000')
pokeInfo = pokeAPI.text  # pulls all the information from the api file and puts in this string variable
poke_json = json.loads(pokeInfo)

for y in poke_json["results"]:
    print(pokemon(y["name"]))
    


# =============================================================================================
# Anime API Code
# =============================================================================================

def anime_ids(animes: list) -> list:
    id_list = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    for anime in animes:
        req = requests.get("https://www.animecharactersdatabase.com/api_series_characters.php?anime_q=" + anime,
                           headers=headers)
        data = json.loads(req.content, strict=False)
        id_list.append(data["search_results"][0]["anime_id"])
    return id_list


# print(anime_ids(["attack on titan"]))

def list_of_gender(pref: str, id: int) -> list:
    char_list = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    req = requests.get("https://www.animecharactersdatabase.com/api_series_characters.php?anime_id=" + str(id),
                       headers=headers)
    data = json.loads(req.content, strict=False)

    for char in data["characters"]:
        if char["gender"] == pref:
            char_list.append(char["name"])
    return char_list


# print(anime_ids(["attack on titan"]))

def anime(animes, gender):
    id_list = anime_ids(animes)
    char_list = []
    for id in id_list:
        for char in list_of_gender(gender, id):
            char_list.append(char)
    return char_list


# print(anime("attack on titan", "male"))
#======================================================================
#Personality QUiz
#======================================================================

#Question, Options, Pokemon/League/Anime
League_Questions = [ 
            "What profession would you prefer your significant other to have?",
            "Are you into normal or slightly weird people?"
            "Is your preference skinny or big people?"
            "Do you like strong but mean or kind but weak people?"
            ]
Professions = ["Fighter", "Mage", "Marksman", "Tank", "support"]
Normal_Weird = ["Normal", "Weird"]
Skinny_Big = ["Skinny", "Big"]
Strong_Weak = ["Strong & Mean", "Kind & Weak"]

Poke_Questions = [
    "What is your favorite color?"
    "What is your favorite element?"
    "What is your favorite shape in a person?"
    "What is your preference in weight?"
    "What is your preference in height?"
]
Colors = ["black", "blue", "brown", "gray", "green", "pink", "purple", "red", "whiet", "yellow"]
Elements = ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel","fire","water","grass","electric","psychic","ice","dragon","dark","fairy"]
Shapes = ["ball","squiggle","fish","arms","blobs","upright","legs","quadruped","wings","tentacles","humanoid"]
Weight = ["Heavy", "Light"]
Height = ["Tall", "Medium", "Short"]
"""

if __name__ == "__main__":  # false if this file imported as module
    # enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run(
        # Comment out on production run
        host="0.0.0.0",
        port=5000,
    )
