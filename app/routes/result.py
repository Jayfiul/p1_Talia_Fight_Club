# Hacks
import sys

sys.path.append("..")

from flask import Blueprint, render_template, request, redirect
from database import user, database
from utils.best_match import get_list_of_characters
from utils import lol_api, poke_api

db=database.Database()

league = lol_api.LOLApi(db)
poke = poke_api.PokeApi(db)

# Create the blueprint
result_bp = Blueprint('result', __name__)


@result_bp.route("/result", methods=['GET', 'POST'])
def result(*args, **kwargs):
    if request.method == "POST":
        chars = get_list_of_characters(db, request.form.get("answers").strip('][').replace('"','').split(','))
        league_chars = chars[0]
        poke_chars = chars[1]
        char_imgs={}
        if league_chars != []:
            for char in league_chars:
                char_imgs[char]=league.get_champion_image(char)
        if poke_chars != []:
            for char in poke_chars:
                db.cur.execute("SELECT image FROM pokemon WHERE name=?", (char,))
                char_imgs[char]=db.cur.fetchall()[0][0]

        return render_template('result.html', imgs=char_imgs)
    else:
        return redirect('/')