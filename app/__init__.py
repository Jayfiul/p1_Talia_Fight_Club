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
from routes.settings import settings_bp
from utils import b64

from utils import lol_api
from utils import poke_api
from utils import anime_api
from utils import lovecalc_api

global db
db = database.Database()


app = Flask(__name__, static_url_path='/static')

app.register_blueprint(home_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(register_bp)
app.register_blueprint(test_bp)
app.register_blueprint(result_bp)
app.register_blueprint(settings_bp)

app.secret_key = b64.base64_encode(
    "this is one hell of a secret key. it's really secure now that we encoded it into base64!")

# TODO: check if need (prolly dont tho)
# global lol_api, poke_api, anime_api, lovecalc_api
# lol_api = lol_api.LOLApi()
# poke_api = poke_api.PokeApi()
# anime_api = anime_api.AnimeApi()

# not assigned to var - already in db after initalization
lol_api.LOLApi(db)
poke_api.PokeApi(db)
anime_api.AnimeApi()

@app.before_request
def before_request():
    request.db = db

if __name__ == "__main__":  # false if this file imported as module
    try:
        # enable debugging, auto-restarting of server when this file is modified
        app.debug = True
        app.run(
            # Comment out on production run
            host="0.0.0.0",
            port=5000,
        )
    except:
        # enable debugging, auto-restarting of server when this file is modified
        app.debug = True
        app.run(
            # Comment out on production run
            host="0.0.0.0",
            port=5001,
        )
