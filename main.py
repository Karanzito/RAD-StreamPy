from js import document, console
from persistent import DB

db = DB()

data = db.load_data()

print("main.py: hello world")

def execute_bind(self, button):

    id = data["id"]
    label = data["label"]

    print(id, label)

    if label == button:
        print(f"{label} == {button}")

    else:
        print(f"{label} != {button}")
    

def on_click(event):
    button = event.target.id
    console.log(f"clicou em: {button}")
    execute_bind(button=button)


for i in range(1, 5):
    button = document.getElementById(f"button_{i}")
    button.onclick = on_click