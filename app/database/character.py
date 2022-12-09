# Character database operations
# DB should be of type cursor


def create_table(db) -> None:
    """
    Creates the characters table

    Args:
        db (Database): The database to create the table in

    Returns:
        None
    """
    db.cur.execute("CREATE TABLE IF NOT EXISTS characters (" +
                   "id INTEGER PRIMARY KEY, " +
                   "name TEXT, " +
                   "category TEXT, " +
                   "qualities TEXT)")
    db.conn.commit()
