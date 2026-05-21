import customtkinter as ctk
from PIL import Image, ImageTk
import os
import ctypes
from pygame import mixer
import threading
import json

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("ControlPainel.StreamPy.1.0")

TITLE = 'StreamPy'
ICON = os.path.join('Images', 'Miku-Halo.ico')
CONFIG_FILE = 'buttons_config.json'

# Inicializar mixer do pygame
mixer.init()

app = ctk.CTk()

icon_image = ImageTk.PhotoImage(Image.open(ICON))

app.title(TITLE)
app.iconphoto(True, icon_image)
app.geometry("800x600")

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
    """Toca um som em thread separada para não travar a interface"""
    def _play():
        try:
            if sound_path not in sounds_cache:
                sounds_cache[sound_path] = mixer.Sound(sound_path)
            sounds_cache[sound_path].play()
        except Exception as e:
            print(f"Erro ao tocar som {sound_path}: {e}")
    
    thread = threading.Thread(target=_play, daemon=True)
    thread.start()

def load_buttons_from_json():
    """Carrega os botões do arquivo JSON e cria a interface"""
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
            button_color = button_config.get('color', '#0066FF')
            
            # Validar se o arquivo de som existe
            if not os.path.exists(sound_path):
                print(f"Aviso: Arquivo de som não encontrado: {sound_path}")
            
            # Criar botão
            btn = ctk.CTkButton(
                grid_frame,
                text=button_label,
                command=lambda sp=sound_path: play_sound(sp),
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
