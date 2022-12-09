# Database for our application

import sqlite3


class Database:
    def __init__(self, db="database.db"):
        """
        Creates a database object

        Args:
            db (str): The name of the database file

        Returns:
            Database: The database object
        """
        self.conn = sqlite3.connect(db, check_same_thread=False)
        self.cur = self.conn.cursor()
