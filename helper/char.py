from sqlite.characters import *

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
        return "There was an issue adding your character..."
    