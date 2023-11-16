import sqlite3
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

def get_stats(calling, rank):
    conn = sqlite3.connect("breakrpg.db")
    cur = conn.cursor()
    item = cur.execute(f"SELECT might, deft, grit, insight, aura, attack, hearts FROM calling_ranks WHERE calling = '{calling}' AND rank_num = {rank}").fetchone()
    return item