# Middleware reference
I created an `auth.py` file with a middleware function, `login_required`, that can be attached to any route to require the user to be logged in to access. This is useful for routes that should only be accessible to logged in users, such as the profile page.
The function is used as a decorator on any route that requires the user to be logged in.

Example:
```python
@app.route('/profile')
# This is the middleware decorator ↙️
@login_required(db=db)
def profile():
    return render_template('profile.html')
```