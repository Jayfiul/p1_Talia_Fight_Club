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
                   "question TEXT, " +
                   "choices TEXT, " +
                   "weights TEXT)")
    db.conn.commit()
