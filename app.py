import customtkinter as ctk
import os
import ctypes
from pygame import mixer
import threading
import json
import webbrowser
import serial

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("ControlPainel.StreamPy.1.0")

TITLE = 'StreamPy'
ICON = os.path.join('Images', 'Miku-Halo.ico')
CONFIG_FILE = os.path.join('binds.json')

# Inicializar mixer do pygame
mixer.init()

app = ctk.CTk()

if os.path.exists(ICON):
    try:
        app.iconbitmap(True, ICON)
    except Exception as e:
        print(f"Erro ao carregar ícone: {e}")

app.title(TITLE)
app.geometry("1080x720")

# Frame principal com scroll
main_frame = ctk.CTkFrame(app)
main_frame.pack(expand=True, fill="both", padx=20, pady=20)

# Label de título
title_label = ctk.CTkLabel(main_frame, text=TITLE, font=("Arial", 24, "bold"))
title_label.pack(pady=10)

# Frame para os botões com scroll
canvas = ctk.CTkCanvas(main_frame, bg=app._apply_appearance_mode(app._fg_color))
scrollbar = ctk.CTkScrollbar(main_frame, command=canvas.yview)
scrollable_frame = ctk.CTkFrame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Dicionário para armazenar sons em cache
sounds_cache = {}

def play_sound(sound_path):

    def _play():
        try:
            if sound_path not in sounds_cache:
                sounds_cache[sound_path] = mixer.Sound(sound_path)
            sounds_cache[sound_path].play()
        except Exception as e:
            print(f"❌ Erro ao tocar som {sound_path}: {e}")
    
    thread = threading.Thread(target=_play, daemon=True)
    thread.start()

def open_application(app_path):

    def _open():
        try:
           
            os.startfile(app_path)
    
            print(f"✅ Aplicativo aberto: {app_path}")
        except Exception as e:
            print(f"❌ Erro ao abrir aplicativo {app_path}: {e}")
    
    thread = threading.Thread(target=_open, daemon=True)
    thread.start()

def open_url(url):
    """Abre uma URL no navegador padrão em thread separada"""
    def _open():
        try:
            # Garantir que a URL tenha protocolo
            if not url.startswith(('http://', 'https://')):
                url_completa = f'https://{url}'
            else:
                url_completa = url
            
            webbrowser.open(url_completa)
            print(f"✅ URL aberta no navegador: {url_completa}")
        except Exception as e:
            print(f"❌ Erro ao abrir URL {url}: {e}")
    
    thread = threading.Thread(target=_open, daemon=True)
    thread.start()

def execute_action(button_config):
    """Executa a ação do botão (som, aplicativo e/ou URL)"""
    # Tocar som se configurado
    sound_path = button_config.get('sound', '')
    if sound_path and os.path.exists(sound_path):
        play_sound(sound_path)
    
    # Abrir aplicativo se configurado
    app_path = button_config.get('app', '')
    if app_path:
        open_application(app_path)
    
    # Abrir URL se configurada
    url = button_config.get('url', '')
    if url:
        open_url(url)

def load_buttons_from_json():

    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        buttons_config = config.get('buttons', [])
        
        if not buttons_config:
            label = ctk.CTkLabel(scrollable_frame, text="Nenhum botão configurado", font=("Arial", 14))
            label.pack(pady=20)
            return
        
        # Criar grid de botões (4 colunas)
        grid_frame = ctk.CTkFrame(scrollable_frame)
        grid_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        for idx, button_config in enumerate(buttons_config):
            row = idx // 4
            col = idx % 4
            
            button_label = button_config.get('label', 'Button')
            sound_path = button_config.get('sound', '')
            app_path = button_config.get('app', '')
            url = button_config.get('url', '')
            button_color = button_config.get('color', '#0066FF')
            
            # Validações
            if sound_path and not os.path.exists(sound_path):
                print(f"⚠️ Arquivo de som não encontrado: {sound_path}")
            
            if app_path and not os.path.exists(app_path):
                print(f"⚠️ Aplicativo não encontrado: {app_path}")
            
            # Criar botão
            btn = ctk.CTkButton(
                grid_frame,
                text=button_label,
                command=lambda bc=button_config: execute_action(bc),
                fg_color=button_color,
                hover_color=button_color,
                text_color="white",
                font=("Arial", 14, "bold"),
                height=80,
                width=150
            )
            btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        
        # Configurar pesos das colunas
        for col in range(4):
            grid_frame.grid_columnconfigure(col, weight=1)
    
    except FileNotFoundError:
        label = ctk.CTkLabel(scrollable_frame, text=f"Arquivo {CONFIG_FILE} não encontrado!", font=("Arial", 14), text_color="red")
        label.pack(pady=20)
    except json.JSONDecodeError:
        label = ctk.CTkLabel(scrollable_frame, text="Erro ao ler o JSON!", font=("Arial", 14), text_color="red")
        label.pack(pady=20)
    except Exception as e:
        label = ctk.CTkLabel(scrollable_frame, text=f"Erro: {str(e)}", font=("Arial", 14), text_color="red")
        label.pack(pady=20)

# Carregar botões ao iniciar
load_buttons_from_json()

# Frame inferior com botões de controle
control_frame = ctk.CTkFrame(main_frame)
control_frame.pack(fill="x", pady=10)

def reload_buttons():
    """Recarrega os botões do JSON"""
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    load_buttons_from_json()

reload_btn = ctk.CTkButton(control_frame, text="Recarregar", command=reload_buttons)
reload_btn.pack(side="left", padx=5)

stop_btn = ctk.CTkButton(control_frame, text="Parar Som", command=mixer.stop)
stop_btn.pack(side="left", padx=5)

app.mainloop()