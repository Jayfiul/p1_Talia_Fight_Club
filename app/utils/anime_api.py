import requests
import json

class AnimeApi:
    def __init__(self):
        self.anime_url = 'https://www.animecharactersdatabase.com/api_series_characters.php?anime_id='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

        }

    def anime_ids(self, animes: list) -> list:
        id_list = []
        for anime in animes:
            req = requests.get("https://www.animecharactersdatabase.com/api_series_characters.php?anime_q=" + anime,
                               headers=self.headers)
            data = json.loads(req.content, strict=False)
            id_list.append(data["search_results"][0]["anime_id"])
        return id_list

    def list_of_gender(self, pref: str, id: int) -> list:
        char_list = []
        req = requests.get("https://www.animecharactersdatabase.com/api_series_characters.php?anime_id=" + str(id),
                           headers=self.headers)
        data = json.loads(req.content, strict=False)

        for char in data["characters"]:
            if pref == "either":
                char_list.append(char["name"])

            if char["gender"] == pref:
                char_list.append(char["name"])
        return char_list
