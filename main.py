from js import document, console

print("main.py: hello world")

def on_click(event):
    button = event.target.id
    console.log(f"clicou em: {button}")


for i in range(1, 5):
    button = document.getElementById(f"button_{i}")
    button.onclick = on_click