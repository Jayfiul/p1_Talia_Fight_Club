import json

def league_match(db, answers):
    if answers==[]:
        return []
    
    db.cur.execute("SELECT name FROM league WHERE (weird=? AND weight=? AND strength=?)",
                   (answers[1],answers[2],answers[3]))
    
    out=[]
    for item in db.cur.fetchall():
        out.append(item[0])
    return out

def poke_match(db, answers):
    if answers==[]:
        return []
    db.cur.execute("SELECT name FROM pokemon WHERE (color=? AND shape=? AND heavy=? AND height=?)",
                   (answers[0],answers[2],answers[3],answers[4]))
    out=[]
    for item in db.cur.fetchall():
        if item[0] not in out:
            out.append(item[0])
    return out


def get_list_of_characters(db, answers: list) -> list:
    with open("cache/questions.json") as json_file:
        questions = json.loads(json_file.read())
     
    # parse for type, split answers
    league_ans = []
    poke_ans = []
    anime_ans = []
    for answer in answers:
        for question in questions:
            if answer in question["answers"]:
                if question["type"] == "league-of-legends":
                    league_ans.append(answer)
                elif question["type"] == "pokemon":
                    poke_ans.append(answer)
                else:
                    anime_ans.append(answer)
    return (league_match(db, league_ans), poke_match(db, poke_ans))
        



def match(username, session):
    pass
# check session
# reference something
# reference getting from tbl
# TODO: fix anime.py