import pyautogui
import time

def clicar_em(tecla_f, coordenadas):
    x, y = coordenadas[tecla_f]
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.click()
    time.sleep(0.1)