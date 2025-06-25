import threading

def on_press(event, teclas_mapeadas, coordenadas, clicar_em):
    tecla = event.name
    if tecla in teclas_mapeadas:
        tecla_f = teclas_mapeadas[tecla]
        threading.Thread(target=clicar_em, args=(tecla_f, coordenadas), daemon=True).start()
