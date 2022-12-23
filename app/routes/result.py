# Hacks
import sys

sys.path.append("..")

from flask import Blueprint, render_template, request, session, redirect
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

 

    # Fetch the user from the database
    if "username" in session:
        user_data = user.get_user(db, session["username"])
        if len(user_data) > 0:
            user_data = user.convert_to_user(user_data[0])
        else:
            user_data = None

    if "username" in session:
        return render_template("result.html", user=user_data)
    else:
        return render_template("index_guest.html")

'''
# Parse answers for each type
        lol_answers = []
        pokemon_answers = []
        anime_answers = []
        # Get the user's answers (JSON string from answers field)
        answers = request.form.get("answers")
        # Parse the JSON string into a dictionary
        answers = json.loads(answers)
        # Print the answers
        print(answers)
        # Loop through each question
        for answer in range(len(answers)):
            # Get the question
            question = questions_filtered[answer]
            # Get the user's answer
            user_answer = answers[answer]
            # Get the type of question
            question_type = question["type"]
            # Append the answer to the correct list
            if question_type == "league-of-legends":
                lol_answers.append([user_answer])
            elif question_type == "pokemon":
                pokemon_answers.append([user_answer])
            elif question_type == "anime":
                anime_answers.append([user_answer])

        # Get the best match for each type
        lol_best_match = best_match(lol_answers, "league-of-legends")
        pokemon_best_match = best_match(pokemon_answers, "pokemon")
        anime_best_match = best_match(anime_answers, "anime")

        # Get characters for each answer
        return render_template("result.html", answers=answers, questions=questions, allowed_types=allowed_types, results=results)
        '''