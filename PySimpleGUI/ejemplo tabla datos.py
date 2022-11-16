import PySimpleGUI as sg
import pandas as pd

def crearVentanaDatos():
    datos = pd.read_csv("Adquisiciones_realizadas.csv")
    columnas = datos.columns.tolist()
    muestra = datos.head(10).values.tolist()
    suma = datos[" Monto_Total_Sin_IVA "].sum()
    layout = [
        [sg.Text("Tabla de datos")],
        [sg.Table(headings=columnas, values=muestra)],
        [sg.Text(f"Suma total de montos: ${suma:,.2f}")]
        ]
    return sg.Window("Mi ventana con datos", layout, finalize=True)

ventanaDatos = crearVentanaDatos()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break