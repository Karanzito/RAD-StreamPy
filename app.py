import dearpygui.dearpygui as dpg
import os
import ctypes
from playsound import playsound
import threading

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("ControlPainel.Soudboard.1.0") # prevents generic python icon in the taskbar

icon = os.path.join('Images', 'Miku-Halo.ico')

sounds = [f'{os.path.join('souds', 'gawr-gura.mp3')}']

def play_sound(sender, app_data, user_data):
    threading.Thread( # separar em thread para não congelar ui
        target=playsound,
        args=(user_data,),
        daemon=True
    ).start()

def add_soud_button(name, file):

    sounds.append({
        "nome": name,
        "file": file
    })

    dpg.add_button(
        label=name,
        parent="container_sons",
        callback=play_sound,
        user_data=file
    )

def create_soud_button():
    name = f"sound {len(sounds) + 1}"
    file = '.\sounds\gawr-gura.mp3'

    add_soud_button(name=name, file=file)

    

dpg.create_context()

with dpg.theme() as plus_button:

    with dpg.theme_component(dpg.mvButton):

        # cor normal
        dpg.add_theme_color(
            dpg.mvThemeCol_Button,
            (180, 50, 50),
            category=dpg.mvThemeCat_Core
        )

with dpg.window(
    label='Soudboard', 
    tag='main_window'):

    dpg.add_text('hello world')
    plus_soudboard_button = dpg.add_button(label='+', callback=create_soud_button())
    dpg.bind_item_theme(plus_soudboard_button, plus_button)

    dpg.add_separator()

    with dpg.child_window(
        label='souds',
        tag='soud_window', 
        autosize_x=True, 
        auto_resize_y=True
    ):
        pass

dpg.create_viewport(title='Soudboard')

dpg.set_viewport_small_icon(icon=icon)
dpg.set_viewport_large_icon(icon=icon)
        
dpg.setup_dearpygui()
dpg.show_viewport()

dpg.set_primary_window('main_window', True)

dpg.start_dearpygui()
dpg.destroy_context()
