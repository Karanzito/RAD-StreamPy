import os
from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS

from persistent import DB 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder=BASE_DIR, static_url_path='')
CORS(app) 


db = DB() 

@app.route("/")
def index():
    
    return send_from_directory(BASE_DIR, 'index.html')

@app.route("/data")
def data():
    dados_do_banco = db.get_data() 
    return jsonify(dados_do_banco)


@app.route("/save", methods=["POST"])
def save_data():
    try:
        updated_data = request.json # This gets the json_payload from your frontend
        
        # We call the save method in your DB class
        db.save_all_binds(updated_data) 
        
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print(f"Error saving to DB: {e}")

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(BASE_DIR, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)