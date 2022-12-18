# Hacks
# Actual imports
from flask import Flask, request, render_template  # web server essentials

from database import character  # character database operations
from database import database  # main database class
from database import question  # question database operations
from database import user  # user database operations
from database import league
from routes.home import home_bp
from routes.login import login_bp
from routes.logout import logout_bp
from routes.register import register_bp
from routes.test import test_bp
from routes.result import result_bp
from utils import b64

import json
import requests

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


@app.before_request
def before_request():
    request.db = db
    # Get username from session
    request.username = None
    if 'username' in request.cookies:
        request.username = request.cookies['username']
        request.is_logged_in = True

#=======================================================================================================================
#League of Legends API CODE
#=======================================================================================================================
riotAPI = requests.get('http://ddragon.leagueoflegends.com/cdn/12.23.1/data/en_US/champion.json') #api with all the champions in League Info
#print(response_API)

riotInfo = riotAPI.text #pulls all the information from the api file and puts in this string variable
#print(info) #checks out the string of info

riot_json = json.loads(riotInfo) #puts the data into JSON format
#important for later ---> #pictureURL = "http://ddragon.leagueoflegends.com/cdn/12.23.1/img/champion/" + parse_json['data']["Aatrox"]["image"]["full"] #stores the value associated with 'url' in the JSON to variable pictureURL
#print(pictureURL) #checks the image to see it is the correct image

#title = parse_json['data']["Aatrox"]["id"] #retrieves the title of the picture
#print(title)

#Helper function
def tags(attributes): #obtains the league characters' attributes
    tags = [len(attributes)]
    for x in attributes:
        tags.append(x)
    tags.pop(0) #for some reason there is a random number 2, so i need to delete that
    return tags #an example return would be ['Mage', 'Assasin']
#print(tags(parse_json['data']["Ahri"]["tags"])) #tests the tags function above

#Helper function
def partype(partype): #tests the league characters to see if they are normal or weird
    type = "Weird"
    if(partype == "Mana"):
        type = "Normal"
    return type
#print(partype(parse_json['data']["Aatrox"]["partype"])) #tests the tags function above

#Helper function
def weight(armor, spellblock): #tests the league character's bodytype
    weight = "Skinny"
    #print(armor, spellblock) #test
    if(int(armor) > 35 and int (spellblock) > 31):
        weight = "Big"
    return weight
#print(weight(parse_json['data']["Aatrox"]["stats"]["armor"], parse_json['data']["Aatrox"]["stats"]["spellblock"])) 
#tests the tags function above

#Helper function
def strength(attackdamage, attackdamageperlevel): #tests to see if the league character is kind or tough
    strength = "Kind"
    #print(armor, spellblock) #test
    if(int(attackdamage) > 55 or int (attackdamageperlevel) >= 4):
        strength = "Strong"
    return strength
#print(strength(parse_json['data']["Aatrox"]["stats"]["attackdamage"], parse_json['data']["Aatrox"]["stats"]["attackdamageperlevel"])) 
#tests the strength function above

#Helper Function
def league_image(champion):
    file = riot_json['data'][str(champion)]
    image = "http://ddragon.leagueoflegends.com/cdn/12.23.1/img/champion/" + file["image"]["full"]
    return image

#THE MAIN FUNCTION THAT USES ALL THE HELPER FUNCTIONS
def League(champion):
    file = riot_json['data'][str(champion)]
    characteristics = []
    characteristics.append(file["id"])
    characteristics.append(tags(file['tags']))
    characteristics.append(partype(file["partype"]))
    characteristics.append(weight(file["stats"]["armor"], file["stats"]["spellblock"]))
    characteristics.append(strength(file["stats"]["attackdamage"], file["stats"]["attackdamageperlevel"]))
    characteristics.append(league_image(champion))
    return characteristics #Name, Attributes, Weird/Normal, Big/Skinny, Kind/Strong, Image
#print(League("Aatrox"))

for x in riot_json['data']:
    print(League(str(x)))

#=======================================================================================================================
#poke API CODE
#=======================================================================================================================

#Helper Function
def color(name):
    pokeAPI = requests.get('https://pokeapi.co/api/v2/pokemon-species/' + str(name))
    pokeInfo = pokeAPI.text #pulls all the information from the api file and puts in this string variable
    poke_json = json.loads(pokeInfo)
    return poke_json["color"]["name"]

#Helper Function
def shape(name):
    pokeAPI = requests.get('https://pokeapi.co/api/v2/pokemon-species/' + str(name))
    pokeInfo = pokeAPI.text #pulls all the information from the api file and puts in this string variable
    poke_json = json.loads(pokeInfo)
    return poke_json["shape"]["name"]

#Helper Function
def habitat(name):
    pokeAPI = requests.get('https://pokeapi.co/api/v2/pokemon-species/' + str(name))
    pokeInfo = pokeAPI.text #pulls all the information from the api file and puts in this string variable
    poke_json = json.loads(pokeInfo)
    return poke_json["habitat"]["name"]

#def types(types):
#    typeAPI = requests.get('https://pokeapi.co/api/v2/type/' + types)
#    typeInfo = typeAPI.text
#    type_json = json.loads(typeInfo)
#    pokemon = []
#    for x in type_json["pokemon"]:
#        pokemon.append(x["pokemon"]["name"])
#    return pokemon
#print(types("dragon"))

#Helper Function
def heavy(weight):
    if weight > 100:
        weight = "heavy"
    else: weight = "light"
    return weight

#Helper Function
def types(TYPES):
    types = []
    for x in TYPES:
        types.append(x["type"]["name"])
    return types

#Helper Function
def height(heightER):
    if heightER > 20:
        height = "tall"
    elif  heightER > 17:
        height = "medium"
    else: 
        height = "short"
    return height

#Help Function that retrieves the image from the API


#MASTER FUNCTION
def pokemon(name): 
    pokeAPI = requests.get('https://pokeapi.co/api/v2/pokemon-species/' + str(name))
    pokeInfo = pokeAPI.text #pulls all the information from the api file and puts in this string variable
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
    #pokemon.append(poke_json["shape"]["name"])
    #pokemon.append(poke_json["habitat"]["name"])
    #pokemon.append(poke_json["shape"]["name"])
    if(name == "meltan" or name == "melmetal"):
        pokemon.append("NULL")
    else: pokemon.append(poke_json["shape"]["name"])
    pokemon.append(heavy(id_json["weight"]))
    pokemon.append(types(id_json["types"]))
    pokemon.append(height(id_json["height"]))
    pokemon.append(id_json["sprites"]["front_default"]) #tretrieves the image URL

    return pokemon #returns name, id, color, shape, weight, types, height, image
#print(pokemon("dragonite"))

pokeAPI = requests.get('https://pokeapi.co/api/v2/pokemon-species/?offset=0&limit=1000')
pokeInfo = pokeAPI.text #pulls all the information from the api file and puts in this string variable
poke_json = json.loads(pokeInfo)

for y in poke_json["results"]:
    print(pokemon(y["name"]))


#=============================================================================================
#Anime API Code
#=============================================================================================

def anime_ids(animes: list) -> list:
    id_list = []
    headers= {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    for anime in animes:
        req = requests.get("https://www.animecharactersdatabase.com/api_series_characters.php?anime_q="+anime, headers=headers)
        data=json.loads(req.content, strict=False)
        id_list.append(data["search_results"][0]["anime_id"])
    return id_list

#print(anime_ids(["attack on titan"]))

def list_of_gender(pref: str, id: int) -> list:
    char_list = []
    headers= {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    req = requests.get("https://www.animecharactersdatabase.com/api_series_characters.php?anime_id="+str(id), headers=headers)
    data=json.loads(req.content, strict=False)
    
    for char in data["characters"]:
        if char["gender"] == pref:
            char_list.append(char["name"])
    return char_list
#print(anime_ids(["attack on titan"]))

def anime(animes, gender):
    id_list = anime_ids(animes)
    char_list = []
    for id in id_list:
        for char in list_of_gender(gender, id):
            char_list.append(char)
    return char_list
#print(anime("attack on titan", "male"))


if __name__ == "__main__":  # false if this file imported as module
    # enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run(
        host="0.0.0.0",
        port=5000,
    )
