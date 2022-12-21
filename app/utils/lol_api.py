import requests


class LOLApi:
    def __init__(self):
        self.champion_url = 'http://ddragon.leagueoflegends.com/cdn/12.23.1/data/en_US/champion.json'
        self.champion_list = self.get_champion_list()

    def get_champion_list(self):
        response = requests.get(self.champion_url)
        return response.json()['data']

    def get_champion_data(self, champion_name):
        return self.champion_list[champion_name]

    def attributes(self, champion_name):
        tags = self.get_champion_data(champion_name)['tags']
        translations = ["Fighter,Adventurer",
                        "Mage,Wizard",
                        "Marksman,Ranger",
                        "Tank,Paladin",
                        "Assassin,Thief",
                        "Support,Healer"]
        new_tags=[]
        for t in translations:
            one = t.split[0]
            two = t.split[1]
            if one in tags:
                new_tags.append(two)
        return new_tags

    def partype(self, champion_name):
        partype = self.get_champion_data(champion_name)['partype']
        if partype == 'Mana':
            return 'Normal'
        return 'Weird'

    def body_type(self, champion_name):
        # Get armor and spell block
        armor = self.get_champion_data(champion_name)['stats']['armor']
        spell_block = self.get_champion_data(champion_name)['stats']['spellblock']
        if armor > 35 and spell_block > 31:
            return 'Big'
        return 'Skinny'

    def strength(self, champion_name):
        # Get attack damage and attack damage per level
        attack_damage = self.get_champion_data(champion_name)['stats']['attackdamage']
        attack_damage_per_level = self.get_champion_data(champion_name)['stats']['attackdamageperlevel']
        if attack_damage > 55 and attack_damage_per_level > 3:
            return 'Strong'
        return 'Kind'

    def get_champion_image(self, champion_name):
        champion = self.get_champion_data(champion_name)
        image = "https://ddragon.leagueoflegends.com/cdn/12.23.1/img/champion/" + champion['image']['full']
        return image

    def get_champion(self, champion_name):
        characteristics = [
            champion_name,
            self.attributes(champion_name),
            self.partype(champion_name),
            self.body_type(champion_name),
            self.strength(champion_name),
            self.get_champion_image(champion_name)
        ]
        return characteristics

    def get_all_champions(self):
        champions = []
        for champion in self.champion_list:
            champions.append(self.get_champion(champion))
        return champions
