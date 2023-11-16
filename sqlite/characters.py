import sqlite3
""" CREATE TABLE characters (
    user_id INTEGER NOT NULL,
    char_name VARCHAR(255),
    calling VARCHAR(255),
    rank INTEGER,
    species VARCHAR(255),
    size VARCHAR(255),
    might INTEGER,
    deft INTEGER,
    grit INTEGER,
    insight INTEGER,
    aura INTEGER,
    attack INTEGER,
    hearts INTEGER,
    defense INTEGER,
    speed VARCHAR(255)
)
"""

def add_character(user_id, char):
    conn = sqlite3.connect("breakrpg.db")
    cur = conn.cursor()
    item = cur.execute(f"SELECT * from characters WHERE user_id = {user_id}").fetchone()
    if item:
        return False
    
    [might, deft, grit, insight, aura] = char.stats
    defense = 10
    if char.size == 'small':
        deft += 1
        might -= 1
        defense += 1
    elif char.size =='large':
        might += 1
        defense -= 1
    cur.execute(f"""INSERT INTO characters VALUES (
                    {user_id},
                    '{char.name}',
                    '{char.calling}',
                    1,
                    '{char.species}',
                    '{char.size}',
                    {might},
                    {deft},
                    {grit},
                    {insight},
                    {aura},
                    {char.attack},
                    {char.hearts},
                    {defense}
                    '{char.speed}'   
                    )""")
    conn.commit()
    conn.close()
    return True
    
def edit_name(user_id, old_name, new_name):
    conn = sqlite3.connect("breakrpg.db")
    cur = conn.cursor()
    cur.execute(f"""UPDATE characters SET char_name = '{new_name}'
                    WHERE user_id = {user_id} AND char_name = '{old_name}'""")
    conn.commit()
    conn.close()
    
def level_up(user_id, char_name, stats, attack, hearts):
    [might, deft, grit, insight, aura] = stats
    conn = sqlite3.connect("breakrpg.db")
    cur = conn.cursor()
    cur.execute(f"""UPDATE characters
                    SET might = {might}, deft = {deft}, grit = {grit},
                    insight = {insight}, aura = {aura}, attack = {attack},
                    hearts = {hearts}, rank = rank + 1
                    WHERE user_id = {user_id} AND char_name = '{char_name}'""")
    conn.commit()
    conn.close()
    
