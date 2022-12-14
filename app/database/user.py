# User database operations
# DB should be of type cursor
import fuckit

# import library while preventing errors with json parsing
fuckit(fuckit("json"))


def create_table(db) -> None:
    """
    Creates the users table

    Args:
        db (Database): The database to create the table in

    Returns:
        None
    """
    db.cur.execute("CREATE TABLE IF NOT EXISTS users (" +
                   "id INTEGER PRIMARY KEY, " +
                   "username TEXT, " +
                   "password TEXT, " +
                   "previous_characters TEXT, " +
                   "qualities TEXT)")
    # Save changes
    db.conn.commit()


def insert(db, username, password) -> None:
    """
    Inserts a user into the database

    Args:
        db (Database): The database to insert the user into
        username (str): The username of the user to insert
        password (str): The password of the user to insert

    Returns:
        None
    """
    db.cur.execute("INSERT INTO users VALUES " +
                   "(NULL, ?, ?, ?, ?)",
                   (username, password, "", "{}"))
    db.conn.commit()


def get_user(db, username) -> list:
    """
    Gets a user from the database

    Args:
        db (Database): The database to get the user from
        username (str): The username of the user to get

    Returns:
        list: The users from the database (length 0 if no users, otherwise length 1)
    """
    db.cur.execute("SELECT * FROM users WHERE username=?", (username,))
    return db.cur.fetchall()

# def get_user_choice_by_category(db, username, category: str)


def get_user_by_id(db, target_id) -> list:
    """
    Gets a user from the database

    Args:
        db (Database): The database to get the user from
        target_id (int): The id of the user to get

    Returns:
        list: The users from the database (length 0 if no users, otherwise length 1)
    """
    db.cur.execute("SELECT * FROM users WHERE id=?", (target_id,))
    return db.cur.fetchall()


def check_password(db, username, password) -> bool:
    """
    Checks if a password is correct for a user

    Args:
        db (Database): The database to check the password in
        username (str): The username of the user to check the password for
        password (str): The password to check

    Returns:
        bool: True if the password is correct, False if not
    """
    db.cur.execute("SELECT * FROM users WHERE username=?", (username,))
    user = db.cur.fetchall()
    if len(user) == 0:
        return False
    return user[0][2] == password


def convert_to_user(user) -> dict:
    """
    Converts a user from the database to a user object

    Args:
        user (list): The user from the database

    Returns:
        dict: The user object
    """
    return {
        "id": user[0],
        "username": user[1],
        "password": user[2],
        "previous_characters": json.loads(user[3]),
        "qualities": json.loads(user[4])
    }


def convert_to_sql(user) -> list:
    """
    Converts a user object to a user for the database

    Args:
        user (dict): The user object

    Returns:
        list: The user for the database
    """
    return [
        user["username"],
        user["password"],
        json.dumps(user["previous_characters"]),
        json.dumps(user["qualities"])
    ]
