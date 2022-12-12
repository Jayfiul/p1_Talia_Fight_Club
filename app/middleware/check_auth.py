# Hacks
import sys

sys.path.append("..")

from flask import request, redirect, url_for, session  # web server essentials
from database import user


def check_auth():
    if 'username' not in session:
        return redirect(url_for('login'))

    else:
        # Try to get the user from the database
        user_data = user.get_user(request.db, session['username'])

        # If the user doesn't exist, log them out
        if len(user_data) == 0:
            # Redirect the user to the login page
            return redirect('/login')
