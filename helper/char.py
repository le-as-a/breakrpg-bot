from sqlite.characters import *
from sqlite.ranks import *

def calling_info(calling):
    info = {
        'stats': [],
        'attack': 0,
        'hearts': 2,
        'speed': 'average'
    }
    
    match calling:
        case 'Factotum':
            info.stats = [7,9,8,9,9]
        case 'Sneak':
            info.stats = [7,10,7,10,8]
        case 'Champion':
            info.stats = [10, 8, 9, 7, 8]
            info.attack = 1
            info.hearts = 3
        case 'Raider':
            info.stats = [9,9,9,8,7]
            info.attack = 1
            info.hearts = 3
            info.speed = 'fast'
        case 'Battle Princess':
            info.stats = [8,8,9,7,10]
            info.attack = 1
            info.hearts = 3
        case 'Murder Princess':
            info.stats = [8,7,10,8,9]
            info.attack = 1
            info.hearts = 3
        case 'Sage':
            info.stats = [6,8,8,10,8]
        case 'Heretic':
            info.stats = [7,7,10,7,9]
    return info
    
def species_info(species):
    size = 'medium'
    
    if species in ['Chib', 'Goblin']:
        size = 'small'
    elif species in ['Promethean', 'Gruun']:
        size = 'large'
    return size

def new_character(user_id, char):
    status = add_character(user_id, char)
    if status:
        return "Character successfully added!"
    else:
        return "You can only have one character created."
    
def edit_char_name(user_id, old_name, new_name):
    status = edit_name(user_id, old_name, new_name)
    if status:
        return "Name successfully changed."
    else:
        return "Could not find character."
    
def level_up_char(user_id, char_name):
    (calling, rank) = get_char_rank(user_id, char_name)
    (might, deft, grit, insight, aura, attack, hearts) = get_stats(calling, rank)
    status = level_up(user_id, char_name, might, deft, grit, insight, aura, attack, hearts)
    if status:
        return f"{char_name} successfully leveled up from rank {rank} to rank {rank+1}!"
    else:
        return f"There was an error leveling up {char_name}..."