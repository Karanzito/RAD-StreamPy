import sys
import asyncio

# O truque definitivo: pega o módulo que o PyScript injetou diretamente no sistema
try:
    # Tenta o padrão da versão 2024+
    import pyscript
    if hasattr(pyscript, "window"):
        window = pyscript.window
    elif hasattr(pyscript, "js_modules"):
        window = pyscript.js_modules.window
    else:
        # Se falhar, busca direto no dicionário de módulos do Python
        window = sys.modules['pyscript'].window
except Exception:
    # Último recurso se tudo mais falhar (fallback para versões antigas/alternativas)
    from js import window

# Configura os atalhos usando a janela global que encontramos
document = window.document
console = window.console

print("main.py: PyScript finalmente conectado com sucesso!")

API_URL = "http://127.0.0.1:5000/data"

async def load_data():
    try:
        response = await window.fetch(API_URL)
        js_json = await response.json()
        return js_json.to_py()
    except Exception as e:
        print(f"Erro na requisição: {e}")
        return []

def execute_bind(item):
    if item.get('sound') != 'NONE':
        print(f"Tocando som: {item['sound']}")
    if item.get('macro') != 'NONE':
        print(f"Rodando macro: {item['macro']}")
    if item.get('url') != 'NONE':
        print(f"Abrindo URL: {item['url']}")
    if item.get('app') != 'NONE':
        print(f"Abrindo App: {item['app']}")

async def search_bind(button_id):
    data = await load_data()
    
    for item in data:
        label = item.get("label")
        if label == button_id:
            print(f"Sucesso: {label} == {button_id}")
            execute_bind(item)
            return
    print(f"Nenhum comando configurado para o botão {button_id}")

def on_click(event):
    button_id = event.currentTarget.id
    console.log(f"Clicou no botão: {button_id}")
    asyncio.create_task(search_bind(button_id))

# Vincula os eventos nos botões de 1 a 4 do HTML
for i in range(1, 5):
    button = document.getElementById(f"button_{i}")
    if button:
        button.onclick = on_click