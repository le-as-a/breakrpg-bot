import sqlite3
import default_data as data

conn = sqlite3.connect("breakrpg.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS characters")
cur.execute("DROP TABLE IF EXISTS calling_ranks")

table_schemas = [
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
    """,
    """ CREATE TABLE calling_ranks (
        calling VARCHAR(255) NOT NULL,
        rank_num INTEGER,
        might INTEGER,    
        deft INTEGER, 
        grit INTEGER, 
        insight INTEGER, 
        aura INTEGER,
        attack INTEGER, 
        hearts INTEGER
    )"""
]

for x in table_schemas:
    cur.execute(x)
    
# =======

cur.executemany("INSERT INTO calling_ranks VALUES (?,?,?,?,?,?,?,?,?)", data.calling_ranks)

conn.commit()
conn.close()