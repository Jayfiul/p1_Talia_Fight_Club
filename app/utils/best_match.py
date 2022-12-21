def best_match(user_input, possibilities_list):
    # For each possibility, calculate the number of matching fields
    # Return the possibility with the most matching fields
    # If there is a tie, return the first possibility with the most matching fields
    # If there are no matches, return None
    best_choice = None
    best_choice_score = 0
    for possibility in possibilities_list:
        score = 0
        for field in possibility:
            if field in user_input:
                score += 1
        if score > best_choice_score:
            best_choice = possibility
            best_choice_score = score
    return best_choice


def clean_up_lol_list():
    # Get all characters from the database
    lol_api.get_all_characters()
    #