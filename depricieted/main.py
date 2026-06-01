from js import document, console, fetch
import asyncio
from flask import Flask

print("main.py: hello world")

API_URL = "/data"


async def load_data():

    response = await fetch(API_URL)

    data = await response.json()

    return data.to_py()

def execute_bind(item):
    
    if item['sound'] != 'NONE':
        print('play sound')

    if item['macro'] != 'NONE':
        print('play macro')

    if item['url'] != 'NONE':
        print('play url')

    if item['app'] != 'NONE':
        print('play app')

async def search_bind(button):

    data = await load_data()

    for item in data:

        id = item["id"]
        label = item["label"]

        if label == button:
            print(item)
            print(f"{label} == {button}")

            return execute_bind(item)

        else:
            print(f"id:{id}; label:{label} != {button}")
    

def on_click(event):
    button = event.currentTarget.id
    console.log(f"clicou em: {button}")
    asyncio.create_task(search_bind(button))


for i in range(1, 5):
    button = document.getElementById(f"button_{i}")
    button.onclick = on_click