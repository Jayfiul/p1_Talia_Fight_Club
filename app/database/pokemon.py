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
                   "IdS INT, " +
                   "color TEXT, " +
                   "shape TEXT, " +
                   "heavy TEXT, " + 
                   "types TEXT, " +
                   "height TEXT, " +
                   "image TEXT)")
    db.conn.commit()



def insert(db, name, IdS, color, shape, heavy, types, height, image) -> None:
    
    db.cur.execute("INSERT INTO users VALUES " +
                   "(NULL, ?, ?, ?, ?)",
                   (name, IdS, color, shape, heavy, types, height, image))
    db.conn.commit()
