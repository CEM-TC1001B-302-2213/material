import PySimpleGUI as sg
import pandas as pd

def crearVentanaFormulario():
    col1 = sg.Column([
        [sg.Text("Nombre")],
        [sg.Text("Puesto")],
        [sg.Text("Sueldo")],
        [sg.Text("Antigüedad")]
        ])
    col2 = sg.Column([
        [sg.Input(key="input nombre")],
        [sg.Input(key="input puesto")],
        [sg.Input(key="input sueldo")],
        [sg.Input(key="input antigüedad")]
        ])
    layout = [
        [col1, col2],
        [sg.Button("Guardar", key="botón guardar")]
        ]
    return sg.Window("Ventana de datos", layout, finalize=True)

ventanaFormulario = crearVentanaFormulario()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    elif event == "botón guardar":
        datos = pd.read_csv("Empleos.csv")
        nueva_fila = pd.DataFrame([{
            "Nombre": values["input nombre"],
            "Puesto": values["input puesto"],
            "Sueldo": values["input sueldo"],
            "Antigüedad": values["input antigüedad"]
            }])
        datos = pd.concat([datos, nueva_fila], ignore_index=True)
        datos.to_csv("Empleos.csv", index=False)
        sg.Popup("Se ha registrado con éxito", title="¡Éxito!")