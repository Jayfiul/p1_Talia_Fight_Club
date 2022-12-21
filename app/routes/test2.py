# Hacks
import json
import sys

sys.path.append("..")

from flask import Blueprint, render_template, request, session
from database import user

# Create the blueprint
test2_bp = Blueprint('test2', __name__)


@test2_bp.route("/test2", methods=['GET', 'POST'])
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
        # Get the user's answers (JSON string from answers field)
        answers = request.form.get("answers")
        # Parse the JSON string into a dictionary
        answers = json.loads(answers)
        # Print the answers
        print(answers)
        return render_template("test2.html", user=user_data, questions=questions)

    else:
        # Render the quiz page
        return render_template("test2.html", user=user_data, questions=questions)
