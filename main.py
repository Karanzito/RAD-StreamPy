import asyncio
import json
from js import window

document = window.document
console = window.console

print("main.py: hello world!")

API_URL = "http://127.0.0.1:5000/data"
SAVE_URL = "http://127.0.0.1:5000/save"

# total interactable buttons
front_buttons = 6

# edit button
def edit_onclick(event):
    print("edit mode activated.")
    edit_tab = document.getElementById("edit_tab")
    edit_tab.style.display = "block"

    # carrega os dados dos botões
    asyncio.create_task(show_edit_tab(edit_tab=edit_tab))


async def show_edit_tab(edit_tab):
    data = await load_data()
    edit_content = document.getElementById("edit_content")
    
    # Clean up and build HTML layout in memory (prevents breaking DOM binds)
    html_elements = []
    for idx, item in enumerate(data):
        label = item.get("label", "")
        sound = item.get("sound", "")
        macro = item.get("macro", "")
        url = item.get("url", "")
        app = item.get("app", "")

        html_elements.append(f"""
        <div style='margin-bottom:10px; color:white;'>
          <strong>Bind {idx+1}</strong><br>
          Label: <input id='label_{idx}' type='text' value='{label}'><br>
          Sound: <input id='sound_{idx}' type='text' value='{sound}'><br>
          Macro: <input id='macro_{idx}' type='text' value='{macro}'><br>
          URL: <input id='url_{idx}' type='text' value='{url}'><br>
          App: <input id='app_{idx}' type='text' value='{app}'><br>
        </div>
        """)
    
    edit_content.innerHTML = "".join(html_elements)

    # botão fechar
    close_btn = document.getElementById("close_edit")
    close_btn.onclick = lambda e: setattr(edit_tab.style, "display", "none")

    # botão salvar logic
    async def save_handler(e):
        updated_data = []
        for idx, original_item in enumerate(data):
            updated_item = {
                "id": original_item.get("id"), # Relies on backend identifier to update target rows
                "label": document.getElementById(f"label_{idx}").value,
                "sound": document.getElementById(f"sound_{idx}").value,
                "macro": document.getElementById(f"macro_{idx}").value,
                "url": document.getElementById(f"url_{idx}").value,
                "app": document.getElementById(f"app_{idx}").value,
            }
            updated_data.append(updated_item)
        
        console.log("Enviando dados atualizados para o Flask...")
        
        try:
            # Serializes cleanly using Python json utility before passing to fetch body
            json_payload = json.dumps(updated_data)

            response = await window.fetch(
                SAVE_URL, 
                method="POST", 
                headers={"Content-Type": "application/json"},
                body=json_payload
            )
            
            if response.ok:
                console.log("Dados salvos com sucesso!")
                edit_tab.style.display = "none"
            else:
                console.error("Erro na resposta do servidor.")
        except Exception as err:
            console.error(f"Erro ao salvar dados: {err}")

    save_btn = document.getElementById("save_edit")
    save_btn.onclick = lambda e: asyncio.create_task(save_handler(e))


# binded buttons loader
async def load_data():
    try:
        response = await window.fetch(API_URL)
        js_json = await response.json()
        return js_json.to_py()
    except Exception as e:
        console.log(f"Erro ao buscar dados do Flask: {e}")
        return []


def execute_bind(item):
    if item.get('sound') and item.get('sound') != 'NONE':
        print(f"Play som: {item['sound']}")

    if item.get('macro') and item.get('macro') != 'NONE':
        print(f"Play macro: {item['macro']}")

    if item.get('url') and item.get('url') != 'NONE':
        print(f"Play url: {item['url']}")

    if item.get('app') and item.get('app') != 'NONE':
        print(f"Play app: {item['app']}")


async def search_bind(button_id):
    data = await load_data()

    for item in data:
        item_label = item.get("label")
        if item_label == button_id:
            print(f"btn: <{button_id}> = label: {item_label}")
            execute_bind(item)
            return
    
    print(f"item: <{button_id}> not found in <data>")


def on_click(event):
    button_id = event.currentTarget.id
    console.log(f"Click: {button_id}")
    asyncio.create_task(search_bind(button_id))


# Loop binding configuration
for i in range(1, front_buttons + 1): # Fixed off-by-one loop limit
    button = document.getElementById(f"button_{i}")
    if button:
        button.onclick = on_click

edit_button = document.getElementById("edit_bind_button")
if edit_button:
    edit_button.onclick = edit_onclick