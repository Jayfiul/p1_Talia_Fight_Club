import requests
import time
from utils.progress_bar import ProgressBar
import json
from database import pokemon


class PokeApi:
    def __init__(self, db):
        self.poke_species_url = 'https://pokeapi.co/api/v2/pokemon-species/'
        self.poke_url = 'https://pokeapi.co/api/v2/pokemon/'
        self.poke_species = self.get_poke_species_list()
        self.poke_list = self.get_poke_list()
        self.cache = {}
        self.species_cache = {}
        self.cache_file = 'cache/poke_cache.json'
        # load cache
        try:
            self.load_cache()
        except:
            pass

        self.get_all_pokemon()
        for poke in self.poke_list:
            attr = self.get_pokemon(poke['name'])
            pokemon.insert(db, attr[0], attr[1], attr[2], attr[3], ",".join(attr[4]), attr[5], attr[6])

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
                poke_data = requests.get(self.poke_url + poke_name)
                full_poke_data = poke_data.json()
                new_poke_data = {}
                new_poke_data['name'] = full_poke_data['name']
                new_poke_data['id'] = full_poke_data['id']
                new_poke_data['height'] = full_poke_data['height']
                new_poke_data['weight'] = full_poke_data['weight']
                new_poke_data['types'] = full_poke_data['types']
                new_poke_data['img'] = full_poke_data['sprites']['front_default']
                new_poke_data['species'] = full_poke_data['species']['name']
                self.cache[poke_name] = new_poke_data
                return new_poke_data
            except:
                return None

    def get_poke_species_data(self, species_name, force=False):
        if species_name in self.species_cache and not force:
            return self.species_cache[species_name]
        else:
            try:
                poke_data = requests.get(self.poke_species_url + species_name)
                full_poke_data = poke_data.json()
                new_poke_data = {}
                new_poke_data['name'] = full_poke_data['name']
                if (full_poke_data['color'] is not None):
                    new_poke_data['color'] = {"name": full_poke_data['color']['name']}
                if (full_poke_data['shape'] is not None):
                    new_poke_data['shape'] = {"name": full_poke_data['shape']['name']}
                if (full_poke_data['habitat'] is not None):
                    new_poke_data['habitat'] = {"name": full_poke_data['habitat']['name']}
                self.species_cache[species_name] = new_poke_data
                return new_poke_data
            except Exception as e:
                print(e)
                return None

    def get_all_pokemon(self):
        # pokemon = []
        load_progress = ProgressBar(len(self.poke_list))
        progress = 0
        for poke in self.poke_list:
            # pokemon.append(self.get_pokemon(poke['name']))
            progress += 1
            load_progress.update(progress, 'Loaded pokemon: ' + poke['name'] + " (" + str(progress) + "/" + str(
                len(self.poke_list)) + ")")
            if progress % 50 == 0:
                self.save_cache()
                load_progress.update(progress, 'Saved cache: ' + poke['name'] + " (" + str(progress) + "/" + str(
                    len(self.poke_list)) + ")")
        self.save_cache()
        load_progress.finish("Loaded all pokemon")
        # return pokemon

    def save_cache(self):
        obj = {}
        obj['pokemon'] = self.cache
        obj['species'] = self.species_cache
        with open(self.cache_file, 'w') as outfile:
            json.dump(obj, outfile)

    def load_cache(self):
        with open(self.cache_file) as json_file:
            data = json.load(json_file)
            self.cache = data['pokemon']
            self.species_cache = data['species']

    def get_poke_color(self, poke_name):
        if self.get_poke_species_data(self.get_poke_data(poke_name)['species']) is None:
            return None
        return self.get_poke_species_data(self.get_poke_data(poke_name)['species'])['color']['name']

    def get_poke_shape(self, poke_name):
        if self.get_poke_species_data(self.get_poke_data(poke_name)['species']) is None:
            return None
        try:
            return self.get_poke_species_data(self.get_poke_data(poke_name)['species'])['shape']['name']
        except:
            return None

    # def get_poke_habitat(self, poke_name):
    #     if self.get_poke_species_data(self.get_poke_data(poke_name)['species']) is None:
    #         return None
    #     try:
    #         return self.get_poke_species_data(self.get_poke_data(poke_name)['species'])['habitat']['name']
    #     except:
    #         return None

    def get_poke_weight(self, poke_name):
        if self.get_poke_data(poke_name)['weight'] > 100:
            return 'Heavy'
        else:
            return 'Light'

    def get_poke_types(self, poke_name):
        return [x['type']['name'] for x in self.get_poke_data(poke_name)['types']]

    def get_poke_height(self, poke_name):
        if self.get_poke_data(poke_name)['height'] > 20:
            return 'Tall'
        elif self.get_poke_data(poke_name)['height'] > 17:
            return 'Medium'
        else:
            return 'Short'

    def get_pokemon(self, poke_name):
        if self.get_poke_data(poke_name) is None:
            print("returning none whoop whoop")
            return None
        pokemon = []
        pokemon.append(poke_name)
        pokemon.append(self.get_poke_color(poke_name))
        pokemon.append(self.get_poke_shape(poke_name))
        pokemon.append(self.get_poke_weight(poke_name))
        pokemon.append(self.get_poke_types(poke_name))
        pokemon.append(self.get_poke_height(poke_name))
        pokemon.append(self.get_poke_data(poke_name)['img'])
        return pokemon
