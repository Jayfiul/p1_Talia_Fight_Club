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
from database import anime
from database import question
from database import pokemon
from database import league
from database import user

def seed():
    """
    Seeds the database with appropriate tables and data

    Returns:
        None
    """
    print("Are you sure you want to seed the database? This will erase ANY contents in the database (y/n)", end=" ")
    if input().lower() == "y":
        db = database.Database()
        anime.create_table(db)
        pokemon.create_table(db)
        league.create_table(db)
        question.create_table(db)
        user.create_table(db)

        # HANDLED IN JSON FILE PARSED BY JS IN TEMPLATES FILE
        # # -------------------
        # # START QUESTION POP
        # # -------------------
        # def populate_question_table(universe, questions, choices):
        #     for i in range(len(questions)):
        #         question.insert(db, universe, questions[i], choices[i])
        #
        # League_Questions = [
        #     "What fantasy profession would you like to have?",
        #     "Do you like normal or slightly weird people?",
        #     "Is your preference skinny or big people?",
        #     "Do you like strong but mean or kind but weak people?"
        # ]
        #
        # choices = ["Adventurer,Wizard,Ranger,Paladin,Thief,Healer",
        #            "Normal,Weird",
        #            "Skinny,Big",
        #            "Strong & Mean,Kind & Weak"]
        #
        # populate_question_table("League", League_Questions, choices)
        #
        # Poke_Questions = [
        #     "What is your favorite color?",
        #     "What is your favorite element?",
        #     "What is your favorite shape?",
        #     "What is your preference in weight?",
        #     "What is your preference in height?"
        # ]
        # choices = ["black,blue,brown,gray,green,pink,purple,red,white,yellow",
        #            "normal,fighting,flying,poison,ground,rock,bug,ghost,steel,fire,water,grass,electric,psychic,ice,dragon,dark,fairy",
        #            "ball,squiggle,fish,arms,blobs,upright,legs,quadruped,wings,tentacles,humanoid",
        #            "Heavy,Light",
        #            "Tall,Medium,Short"]
        #
        # populate_question_table("Pokemon", Poke_Questions, choices)
        #
        # populate_question_table("Anime", ["What gender do you align with?"], ["Male", "Female", "Either"])
        # # -------------------
        # # END QUESTION POP
        # # -------------------
        print("Seeded database with tables")
    else:
        print("Did not seed database (user cancelled)")

if __name__ == "__main__":
    seed()