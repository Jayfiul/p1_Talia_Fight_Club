# How We Use AnimeCharactersDatabase API

### No API Key Required

### Required Libaries:
```python
import requests
import json
```
### Relation to Personality Test:
- Ask the user what their favorite anime is (up to three): 
  - returns list of all relevant animes
``` python
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

print(anime_ids(["attack on titan"]))
```

- Ask the user if they align more with males or females in __ anime (per anime)
```python
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
```

### Main function: 
- Uses all helper functions to generate a final list of characters given a list of animes and preferred gender
```python
def anime(animes, gender):
    id_list = anime_ids(animes)
    char_list = []
    for id in id_list:
        for char in list_of_gender(gender, id):
            char_list.append(char)
    return char_list
```