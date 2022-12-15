# Character database operations
# DB should be of type cursor


def create_table(db) -> None:
    """
    Creates the pokemon table

    Args:
        db (Database): The database to create the table in

    Returns:
        None
    """
    db.cur.execute("CREATE TABLE IF NOT EXISTS pokemon (" +
                   "id INTEGER PRIMARY KEY, " +
                   "name TEXT, " +
                   "attributes TEXT, " +
                   "weird TEXT, " +
                   "weight TEXT, " +
                   "strength TEXT, " +
                   "image TEXT)")
    db.conn.commit()



def insert(db, name, attributes, weird, weight, strength, image) -> None:
    
    db.cur.execute("INSERT INTO users VALUES " +
                   "(NULL, ?, ?, ?, ?)",
                   (name, attributes, weird, weight, strength, image))
    db.conn.commit()
