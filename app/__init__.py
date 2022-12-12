# Hacks
# Actual imports
from flask import Flask, request  # web server essentials

from database import character  # character database operations
from database import database  # main database class
from database import question  # question database operations
from database import user  # user database operations
from routes.home import home_bp
from routes.login import login_bp
from routes.logout import logout_bp
from routes.register import register_bp
from utils import b64

global db
db = database.Database()

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(register_bp)


@app.before_request
def before_request():
    request.db = db


app.secret_key = b64.base64_encode(
    "this is one hell of a secret key. it's really secure now that we encoded it into base64!")

if __name__ == "__main__":  # false if this file imported as module
    # enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run(
        host="0.0.0.0",
        port=5000,
    )
