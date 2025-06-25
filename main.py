import keyboard
import os
import sys

SRC_DIR = os.path.join(os.path.dirname(__file__), 'src')
if SRC_DIR not in sys.path:
    sys.path.append(SRC_DIR)

from config.settings import caminho_macro
from utils.press import on_press
from utils.click import clicar_em
import os

os.startfile(caminho_macro)

coordenadas = {
    'F1': (997, 289),
    'F2': (993, 323),
    'F3': (986, 366),
    'F4': (972, 414),
    'F5': (980, 465),
    'F6': (979, 501),
    'F7': (679, 200),
    'F8': (677, 491),
}

teclas_mapeadas = {
    'u': 'F1',
    'i': 'F2',
    'o': 'F3',
    'j': 'F4',
    'k': 'F5',
    'l': 'F6',
    'y': 'F7',
    'h': 'F8',
}

print("Rodando. Pressione ESC para sair.")

def handler(event):
    on_press(event, teclas_mapeadas, coordenadas, clicar_em)

keyboard.on_press(handler)

keyboard.wait('esc')

print("Programa encerrado.")
