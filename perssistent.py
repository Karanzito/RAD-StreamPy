import sqlite3 as sql
import os

DATABASE = os.path('Data', 'database.db')

class DB:
    def __init__(self):
        pass

    def load_data(self):
        pass
    
    def save_bind(self):
        pass


def main():

    with sql.connect(DATABASE) as con:
        cur = con.cursor()

        try:

            command = """IF NOT EXISTS CREATE TABLE DATA (
            id PRIMARY KEY AUTOINCREMENT,
            label TEXT UNIQUE,
            sound TEXT DEFAULT NONE,
            macro TEXT DEFAULT NONE,
            url TEXT DEFAULT NONE,
            app TEXT DEFUALT NONE)"""

            cur.execute(command)

            con.commit()

        except Exception as e:
            con.rollback()

            raise Exception(f"Exception Creating TABLE DATA: {e}")
