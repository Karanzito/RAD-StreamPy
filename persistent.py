import sqlite3 as sql
import os

DATABASE = 'database.db'

class DB:
    def __init__(self):
        self.buttons = 4

    def get_data(self):
        with sql.connect(DATABASE) as con:

            print("Connected to database.")
            cur = con.cursor()
            
           
            self.create_table_if_not_exists(cur)
            
            cur.execute('SELECT * FROM DATA')
            row = cur.fetchall()
            
            
            if not row:
                self.populate_default_data(cur, con)
                cur.execute('SELECT * FROM DATA')
                row = cur.fetchall()

            data = []
            for i in row:
                data.append({
                    "id": i[0],
                    "label": i[1],
                    "sound": i[2],
                    "macro": i[3],
                    "url": i[4],
                    "app": i[5]
                })
        return data

    def create_table_if_not_exists(self, cur):

        command = """CREATE TABLE IF NOT EXISTS DATA (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        label TEXT UNIQUE,
        sound TEXT DEFAULT 'NONE',
        macro TEXT DEFAULT 'NONE',
        url TEXT DEFAULT 'NONE',
        app TEXT DEFAULT 'NONE')"""

        cur.execute(command)

    def populate_default_data(self, cur, con):

        print("populate defaults.")
        values = [(f'button_{b}',) for b in range(1, self.buttons + 1)]
        default_insert = f"""INSERT OR IGNORE INTO DATA (label) VALUES (?)"""

        cur.executemany(default_insert, values)
        con.commit()

    def save_data(self, data):
        with sql.connect(DATABASE) as con:
            cur = con.cursor()

            cmd = """
            UPDATE DATA 
            SET sound = ?, 
                macro = ?, 
                url = ?, 
                app = ? 
            WHERE id = ?
            """

            for item in data:
                row_id = item.get("id")
                if row_id is None:
                    print(f"Warning: Skipping item because it lacks an 'id' key: {item}")
                    continue

                params = (
                    item.get("sound", ""),
                    item.get("macro", ""),
                    item.get("url", ""),
                    item.get("app", ""),
                    row_id
                )

                cur.execute(cmd, params)

            con.commit()





db = DB()
        
if __name__ == '__main__':
    self = DB()
    buttons = DB().buttons
    print(buttons, type(buttons))

    self.load_data()