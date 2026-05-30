import sqlite3 as sql
import os

DATABASE = os.path.join('Data', 'database.db')

class DB:
    def __init__(self):
        buttons = 4
        self.buttons = buttons

    def default_data(self):

        with sql.connect(DATABASE) as con:
                cur = con.cursor()
                
                cur.execute('SELECT * FROM DATA')
                row = cur.fetchall()

                print(row)

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

                print(f"data:\n {data}")

                return data

    def load_data(self):
    
        try:
            data = self.default_data()

            return data   
            
        except sql.OperationalError as e:
            
            if 'no such table' in str(e):
                print(f'Table <DATA> not found\ncreating default table...')

            else:
                print(f'Error: {e}\nrestoring default table...')

            print(self.buttons)

            self.main(buttons=self.buttons)

            data = self.default_data()

        except Exception as e:
            raise Exception(f'Exception in <load_data()>: {e}')
    
    def save_bind(self, id, label, sound, macro, url, app):

        with sql.connect(DATABASE) as con:

            try:
                cur = con.cursor()

                values = ((label, sound, macro, url, app),)

                cur.execute("""UPDATE DATA SET (
                        label = ?, 
                        sound = ?,  
                        macro = ?, 
                        url = ?, 
                        app = ?)
                        WHERE id = ?""", values)
                
                con.commit()

            except Exception as e:
                con.rollback()

                raise Exception(e)


    def main(buttons):

        with sql.connect(DATABASE) as con:
            cur = con.cursor()

            try:

                command = """CREATE TABLE IF NOT EXISTS DATA (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                label TEXT UNIQUE,
                sound TEXT DEFAULT 'NONE',
                macro TEXT DEFAULT 'NONE',
                url TEXT DEFAULT 'NONE',
                app TEXT DEFAULT 'NONE')"""

                cur.execute(command)

                values = [(f'button_{b}',) for b in range(1, buttons + 1)]

                print(f'values = {values}')

                default_insert = f"""INSERT INTO DATA (label) VALUES (?)"""

                cur.executemany(default_insert, values)

                con.commit()

            except Exception as e:
                con.rollback()

                raise Exception(f"Exception Creating TABLE <DATA>: {e}")
            
print("hello world")
        
if __name__ == '__main__':
    self = DB()
    buttons = DB().buttons
    print(buttons, type(buttons))

    # self.main(buttons)

    self.load_data()