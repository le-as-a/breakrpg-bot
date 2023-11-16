import sqlite3

conn = sqlite3.connect("breakrpg.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS characters")

table_schemas = [
    """ CREATE TABLE characters (
        user_id INTEGER NOT NULL,
        char_name VARCHAR(255),
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
]

for x in table_schemas:
    cur.execute(x)

conn.commit()
conn.close()