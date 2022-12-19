import requests


class PokeApi:
    def __init__(self):
        self.poke_species_url = 'https://pokeapi.co/api/v2/pokemon-species/'
        self.poke_url = 'https://pokeapi.co/api/v2/pokemon/'
        self.poke_species = self.get_poke_species_list()
        self.poke_list = self.get_poke_list()
        self.cache = {}

    def get_poke_species_list(self):
        response = requests.get(self.poke_species_url)
        count = response.json()['count']
        response = requests.get(self.poke_species_url + '?limit=' + str(count))
        return response.json()['results']

    def get_poke_list(self):
        response = requests.get(self.poke_url)
        count = response.json()['count']
        response = requests.get(self.poke_url + '?limit=' + str(count))
        return response.json()['results']

    def get_poke_data(self, poke_name, force=False):
        if poke_name in self.cache and not force:
            return self.cache[poke_name]
        else:
            poke_data = requests.get(self.poke_species_url + poke_name).json()
            self.cache[poke_name] = poke_data
            return poke_data

    def get_poke_color(self, poke_name):
        return self.get_poke_data(poke_name)['color']['name']

    def get_poke_shape(self, poke_name):
        return self.get_poke_data(poke_name)['shape']['name']

    def get_poke_habitat(self, poke_name):
        return self.get_poke_data(poke_name)['habitat']['name']

    def get_poke_weight(self, poke_name):
        if self.get_poke_data(poke_name)['weight'] > 100:
            return 'heavy'
        else:
            return 'light'

    def get_poke_types(self, poke_name):
        return [x['type']['name'] for x in self.get_poke_data(poke_name)['types']]

    def get_poke_height(self, poke_name):
        if self.get_poke_data(poke_name)['height'] > 20:
            return 'tall'
        elif self.get_poke_data(poke_name)['height'] > 17:
            return 'medium'
        else:
            return 'short'

    """
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
    """

