# How We Use pokeAPI

### No API Key Required

### Relation to Personality Test:
- Ask the user what their favorite color is
- Ask the user what their least favorite color is
```
def color(name):
    pokeAPI = requests.get('https://pokeapi.co/api/v2/pokemon-species/' + str(name))
    pokeInfo = pokeAPI.text #pulls all the information from the api file and puts in this string variable
    poke_json = json.loads(pokeInfo)
    return poke_json["color"]["name"]
```

- Ask the user what their favorite element is
    - Fire, Ice, Dragon, Water, etc.
```
def types(id):
    typesAPI = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(id))
    typesInfo = typesAPI.text
    types_json = json.loads(typesInfo)
    types = []
    for x in types_json["types"]:
        types.append(x["type"]["name"])
    return types
```

- Ask the user what their favorite habitat is
    - Hot, Cold, Ocean, City
```
def habitat(name):
    pokeAPI = requests.get('https://pokeapi.co/api/v2/pokemon-species/' + str(name))
    pokeInfo = pokeAPI.text #pulls all the information from the api file and puts in this string variable
    poke_json = json.loads(pokeInfo)
    return poke_json["habitat"]["name"]
```

- Ask the user what their favorite shape is
  - Ex: quadrupled
```
def shape(name):
    pokeAPI = requests.get('https://pokeapi.co/api/v2/pokemon-species/' + str(name))
    pokeInfo = pokeAPI.text #pulls all the information from the api file and puts in this string variable
    poke_json = json.loads(pokeInfo)
    return poke_json["shape"]["name"]
```

- Ask the user what their preference on weight is:
  - Heavy or Light
```
def heavy(id):
    weightAPI = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(id))
    weightInfo = weightAPI.text
    weight_json = json.loads(weightInfo)
    if weight_json["weight"] > 100:
        weight = "heavy"
    else: weight = "light"
    return weight
```

- Ask the user what their prefrence on height is:
  - Tall, Average, or Small
```
def height(id):
    weightAPI = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(id))
    weightInfo = weightAPI.text
    weight_json = json.loads(weightInfo)
    if weight_json["height"] > 20:
        height = "tall"
    elif weight_json["height"] > 17:
        height = "medium"
    else: 
        height = "short"
    return height
```


### Master Function
```
def pokemon(name): 
    pokeAPI = requests.get('https://pokeapi.co/api/v2/pokemon-species/' + str(name))
    pokeInfo = pokeAPI.text #pulls all the information from the api file and puts in this string variable
    poke_json = json.loads(pokeInfo)
    pokemon = []
    pokemon.append(poke_json["name"])
    id = int(poke_json["id"])
    pokemon.append(id)
    pokemon.append(color(name))
    pokemon.append(shape(name))
    pokemon.append(habitat(name))
    pokemon.append(heavy(id))
    pokemon.append(types(id))
    pokemon.append(height(id))
    return pokemon
```