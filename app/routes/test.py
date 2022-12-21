# Hacks
import json
import sys

sys.path.append("..")

from flask import Blueprint, render_template, request, session
from database import user
from utils.best_match import best_match

# Create the blueprint
test_bp = Blueprint('test', __name__)


@test_bp.route("/test", methods=['GET', 'POST'])
def test(*args, **kwargs):
    # Fetch the user from the database
    if "username" in session:
        user_data = user.get_user(request.db, session["username"])
        if len(user_data) > 0:
            user_data = user.convert_to_user(user_data[0])
        else:
            user_data = None

    # Load questions from cache/questions.json
    questions = None
    with open("cache/questions.json") as json_file:
        questions = json.load(json_file)

    # If request is POST, then the user is trying to complete the quiz.
    # Otherwise, the user is trying to access the quiz.
    if request.method == "POST":
        # Get allowed types from cookies
        allowed_types = request.cookies.get("allowedQuestions") or "['league-of-legends', 'pokemon', 'anime']"
        allowed_types = json.loads(allowed_types)
        # Sort questions by type
        questions_filtered = []
        for question in questions:
            if question["type"] in allowed_types:
                questions_filtered.append(question)
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

    else:
        # Render the quiz page
        # Get allowed types from cookies
        allowed_types = request.cookies.get("allowedQuestions") or "['league-of-legends', 'pokemon', 'anime']"
        allowed_types = json.loads(allowed_types)
        return render_template("test.html", questions=questions, allowed_types=allowed_types)
