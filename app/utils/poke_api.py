import requests
import time
from utils.progress_bar import ProgressBar

class PokeApi:
    def __init__(self):
        self.poke_species_url = 'https://pokeapi.co/api/v2/pokemon-species/'
        self.poke_url = 'https://pokeapi.co/api/v2/pokemon/'
        self.poke_species = self.get_poke_species_list()
        self.poke_list = self.get_poke_list()
        self.cache = {}
        self.species_cache = {}

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
            try:
                poke_data = requests.get(self.poke_url + poke_name).json()
                self.cache[poke_name] = poke_data
                return poke_data
            except:
                return None

    def get_all_pokemon(self):
        pokemon = []
        load_progress = ProgressBar(len(self.poke_list))
        progress = 0
        for poke in self.poke_list:
            pokemon.append(self.get_pokemon(poke['name']))
            progress += 1
            load_progress.update(progress, 'Loaded pokemon: ' + poke['name'])
        load_progress.finish("Loaded all pokemon")
        return pokemon

    def get_all_pokemon_species(self):
        pokemon = []
        load_progress = ProgressBar(len(self.poke_species))
        progress = 0
        for poke in self.poke_species:
            pokemon.append(self.get_pokemon_species(poke['name']))
            progress += 1
            load_progress.update(progress, 'Loaded pokemon: ' + poke['name'])
        load_progress.finish("Loaded all pokemon")
        return pokemon

    def get_poke_species_data(self, species_name, force=False):
        if species_name in self.species_cache and not force:
            return self.species_cache[species_name]
        else:
            poke_data = requests.get(self.poke_species_url + species_name).json()
            self.species_cache[species_name] = poke_data
            return poke_data

    def get_poke_color(self, poke_name):
        return self.get_poke_species_data(poke_name)['color']['name']

    def get_poke_shape(self, poke_name):
        return self.get_poke_species_data(poke_name)['shape']['name']

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

    def get_pokemon(self, poke_name):
        pokemon = []
        pokemon.append(poke_name)
        pokemon.append(self.get_poke_data(poke_name)['id'])
        pokemon.append(self.get_poke_color(poke_name))
        pokemon.append(self.get_poke_shape(poke_name))
        pokemon.append(self.get_poke_weight(poke_name))
        pokemon.append(self.get_poke_types(poke_name))
        pokemon.append(self.get_poke_height(poke_name))
        pokemon.append(self.get_poke_data(poke_name)['sprites']['front_default'])
        return pokemon
