# Hacks
import json
import sys

sys.path.append("..")

from flask import Blueprint, render_template, request, session, redirect
from database import user

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
        questions = json.loads(json_file.read())
        

    # If request is POST, then the user is trying to complete the quiz.
    # Otherwise, the user is trying to access the quiz.
    if request.method == "POST":
        # # Get allowed types from cookies
        # allowed_types = request.cookies.get("allowedQuestions") or "['league-of-legends', 'pokemon', 'anime']"
        # print(allowed_types)
        # allowed_types = json.loads(allowed_types)
        # get allowed types from form
        allowed_types = request.form.getlist('uni')

        # Sort questions by type
        questions_filtered = []
        for question in questions:
            if question["type"] in allowed_types:
                questions_filtered.append(question)
        return render_template("test.html", questions=questions, allowed_types=allowed_types) #TODO: add is_logged_in

        

    else:
        return redirect('/')
