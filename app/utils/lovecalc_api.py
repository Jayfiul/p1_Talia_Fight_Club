import requests
import json

class loveCalcAPI:
    def __init__(self):
        self.url = "https://love-calculator.p.rapidapi.com/getPercentage"
        with open("keys/key_lovecalc.txt") as f:
            self.headers = {
                "X-RapidAPI-Key": f.read(),
                "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
            }

    def love(self, name1, name2):
        querystring = {"fname": name1, "sname": name2}
        response = requests.request("GET", self.url, headers=self.headers, params=querystring)
        loveInfo = response.text
        love_json = json.loads(loveInfo)
        return love_json["percentage"]  # parses the response.text and returns just the percentage