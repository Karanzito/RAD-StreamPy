import sqlite3 as sql
import os
from flask import Flask, jsonify

DATABASE = 'database.db'
app = Flask(__name__)

class DB:
    def __init__(self):
        self.buttons = 4

    def get_data(self):
        with sql.connect(DATABASE) as con:
            print("Connected to database.")
            cur = con.cursor()
            
            # Garante que a tabela existe antes de tentar ler
            self.create_table_if_not_exists(cur)
            
            cur.execute('SELECT * FROM DATA')
            row = cur.fetchall()
            
            # Se a tabela foi criada agora e está vazia, popula ela
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
        print("Populating default table...")
        values = [(f'button_{b}',) for b in range(1, self.buttons + 1)]
        default_insert = f"""INSERT OR IGNORE INTO DATA (label) VALUES (?)"""
        cur.executemany(default_insert, values)
        con.commit()

db = DB()

# Importante: Permitir CORS se o seu Pyodide estiver rodando em outra porta
@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

@app.route("/data")
def data():
    # Retorna usando jsonify para garantir o cabeçalho application/json correto
    return jsonify(db.get_data())

if __name__ == '__main__':
    app.run(debug=True, port=5000)