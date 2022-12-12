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

<<<<<<< HEAD

@app.route("/")
def home():
    # Fetch the user from the database
    if "username" in session:
        user_data = user.get_user(db, session["username"])
        if len(user_data) > 0:
            user_data = user.convert_to_user(user_data[0])
        else:
            user_data = None

    if "username" in session:
        return render_template("index.html", user=user_data)
    else:
        return render_template("index_guest.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    # If the user is already logged in, redirect them to the home page
    if 'username' in session:
        return redirect(url_for('home'))

    # If it's a POST request, the user is trying to sign up
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Validate the username and password
        if not data_validation.validate_username(username):
            return render_template('register.html', error="Invalid username (a-zA-Z0-9_.-)")
        if not data_validation.validate_password(password):
            return render_template('register.html', error="Invalid password (must be at least 8 characters)")

        # Check if the username is already taken
        if len(user.get_user(db, username)) > 0:
            return render_template('register.html', error="Username already taken")

        # Create the user
        user.insert(db, username, password)

        # Redirect the user to the login page
        session['username'] = username
        return redirect(url_for('home'))

    # If it's a GET request, the user is trying to view the sign up page
    return render_template('register.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    # If the user is already logged in, redirect them to the home page
    if 'username' in session:
        return redirect(url_for('home'))

    # If it's a POST request, the user is trying to log in
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Validate the username and password
        if not data_validation.validate_username(username):
            return render_template('login.html', error="Invalid username (a-zA-Z0-9_.-)")
        if not data_validation.validate_password(password):
            return render_template('login.html', error="Invalid password (must be at least 8 characters)")

        # Check if the username exists
        if len(user.get_user(db, username)) == 0:
            return render_template('login.html', error="Username does not exist")

        # Check if the password is correct
        if not user.check_password(db, username, password):
            return render_template('login.html', error="Incorrect password")

        # Log the user in
        session['username'] = username

        # Redirect the user to the home page
        return redirect(url_for('home'))

    # If it's a GET request, the user is trying to view the login page
    return render_template('login.html')


@app.route("/test", methods=['GET', 'POST'])
#load test page with questions
def test():
    return render_template('test.html')

@app.route("/logout", methods=['GET', 'POST'])
@login_required(db=db)
@fuckit
# Hack so middleware doesn't cause an error with function signature
def logout(*args, **kwargs):
    # If the user is logged in, log them out
    if 'username' in session:
        session.pop('username', None)

    # Redirect the user to the home page
    return redirect(url_for('home'))


=======
>>>>>>> refs/remotes/origin/main
if __name__ == "__main__":  # false if this file imported as module
    # enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run(
        host="0.0.0.0",
        port=5000,
    )
