import PySimpleGUI as sg
import webbrowser

def crearVentanaEnlaces():
    layout = [
        [sg.Button("Mapa", key="botón mapa")],
        [sg.Button("Video", key="botón video")],
        [sg.Button("Podcast", key="botón podcast")]
        ]
    return sg.Window("Ventana enlaces", layout, finalize=True)

ventanaEnlaces = crearVentanaEnlaces()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    elif event == "botón mapa":
        webbrowser.open("https://www.google.com/maps/d/edit?mid=1vslDYkw-d5mz1XQjSP2wRKPl9e0REas&usp=sharing")
    elif event == "botón video":
        webbrowser.open("https://www.youtube.com/watch?v=21X5lGlDOfg")