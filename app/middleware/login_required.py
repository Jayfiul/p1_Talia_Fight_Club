# Hacks
import sys

sys.path.append("..")

# Actual imports
from functools import wraps
from flask import redirect, url_for, session
from database import user


def login_required(db):
    """
    Decorator to check if the user is logged in

    Args:
        func (function): The function to decorate

    Returns:
        function: The decorated function
    """

    def wrap(f):
        @wraps(f)
        def wrapped_function(*args, **kwargs):
            if 'username' not in session:
                return redirect(url_for('login'))

            else:
                # Try to get the user from the database
                user_data = user.get_user(db, session['username'])

                # If the user doesn't exist, log them out
                if len(user_data) == 0:
                    # Redirect the user to the login page
                    return redirect(url_for('login'))

                # If the user exists, pass the user object to the function
                else:
                    return f(user_data[0], *args, **kwargs)
            return f(*args, **kwargs)

        return wrapped_function

    return wrap
