# Question database operations
# DB should be of type cursor

def create_table(db) -> None:
    """
    Creates the questions table

    Args:
        db (Database): The database to create the table in

    Returns:
        None
    """
    db.cur.execute("CREATE TABLE IF NOT EXISTS questions (" +
                   "id INTEGER PRIMARY KEY, " +
                   "universe TEXT" +
                   "question TEXT, " +
                   "choices TEXT, " +
                   "weights TEXT)")
    db.conn.commit()

def insert(db, universe, question, choices) -> None:
    """
        Inserts a question into the database

        Args:
            db (Database): The database to insert the user into
            universe (str): The universe to which the question belongs to
            question (str): The question being asked
            choices (str): The choices to the question as csv
            weights (str): What each choice means as csv

        Returns:
            None
    """
    db.cur.execute("INSERT INTO questions VALUES " +
                   "(NULL, ?, ?, ?)",
                   (universe, question, choices))
    db.conn.commit()