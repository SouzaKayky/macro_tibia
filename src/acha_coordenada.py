import pyautogui
import keyboard

coordenadas = {}

def capturar_coordenada(tecla_nome):
    pos = pyautogui.position()
    coordenadas[tecla_nome] = pos
    print(f"Coordenada para '{tecla_nome}' salva: {pos}")

print("Posicione o mouse e pressione F1, F2, F3, F4, F5,F6 para capturar coordenadas.")
print("Pressione ESC para sair e ver todas as coordenadas salvas.")

teclas = ['F1','F2', 'F3', 'F4', 'F5','F6']

for tecla in teclas:
    keyboard.add_hotkey(tecla, lambda t=tecla: capturar_coordenada(t))

keyboard.wait('esc')

print("\nCoordenadas capturadas:")
for tecla, pos in coordenadas.items():
    print(f"{tecla}: {pos}")

input("\nPressione ENTER para sair...")
