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
                   "color TEXT, " +
                   "shape TEXT, " +
                   "habitat TEXT, " +
                   "heavy TEXT, " + 
                   "types TEXT, " +
                   "image TEXT, " +
                   "height TEXT)")
    db.conn.commit()



def insert(db, name, color, shape, habitat, heavy, types, height) -> None:
    
    db.cur.execute("INSERT INTO users VALUES " +
                   "(NULL, ?, ?, ?, ?)",
                   (name, color, shape, habitat, heavy, types, height))
    db.conn.commit()
