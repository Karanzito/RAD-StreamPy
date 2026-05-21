import json
import serial

JS_FILE = 'binds.json'

default_data = {"sounds": []}

class Perssitent:

    def create_new_bind(label, sound, color):

        with open(JS_FILE, 'r') as js_f:
            data = json.load(js_f)
        
        print(data)

