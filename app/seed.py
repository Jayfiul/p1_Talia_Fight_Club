# Seed our database with appropriate tables and data
"""
Table: Users
id
int
username
string
password
string (are we hashing?)
previous_characters
string (separated by commas)
qualities
string (JSON)


Table: characters
id
int
name
string
category
string
qualities
String (JSON)


Table: questions
id
int
question
string
choices
String (JSON)
weights
String (JSON)
"""

from database import database

from database import user
from database import character
from database import question
from database import pokemon
from database import league

def seed():
    """
    Seeds the database with appropriate tables and data

    Returns:
        None
    """
    print("Are you sure you want to seed the database? This will erase ANY contents in the database (y/n)", end=" ")
    if input().lower() == "y":
        db = database.Database()
        user.create_table(db)
        pokemon.create_table(db)
        league.create_table(db)
        #character.create_table(db)
        question.create_table(db)
        print("Seeded database with tables (this may or may not have worked)")
    else:
        print("Did not seed database (user cancelled)")

if __name__ == "__main__":
    seed()