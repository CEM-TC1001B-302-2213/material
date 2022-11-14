import PySimpleGUI as sg

def crearVentanaPrincipal():
    layout = [
        [sg.Text("Mi primer texto",
                 font="Arial 30",
                 text_color="yellow",
                 background_color="purple"),
         sg.Text("Soy otro texto")],
        [sg.Button("Soy un botón",
                   key="botón1",
                   image_filename="eevee.png"),
         sg.Button("Soy el otro botón",
                   key="botón2")],
        [sg.Text("Correo"),
         sg.Input(key="input correo",
                  default_text="Introduce tu correo...")],
        [sg.Text("Contraseña"),
         sg.Input(key="input contraseña",
                  password_char="*")],
        [sg.Text("Estado de vacunación"),
         sg.Radio("Sí estoy vacunado",
                  key="radio vacunación sí",
                  group_id="vacunación group"),
         sg.Radio("No estoy vacunado",
                  key="radio vacunación no",
                  group_id="vacunación group",
                  default=True)]
        ]
    return sg.Window("Mi primera ventana", layout, finalize=True)

ventanaPrincipal = crearVentanaPrincipal()

while True:
    window, event, values = sg.read_all_windows()
    #print(f"Window: {window}")
    #print(f"Event: {event}")
    #print("Values: {values}")
    
    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    elif event == "botón1":
        print("Dieron click en el botón 1")
        correo = values["input correo"]
        contraseña = values["input contraseña"]
        print(f"Correo: {correo} - Contraseña: {contraseña}")
        vacunado_sí = values["radio vacunación sí"]
        vacunado_no = values["radio vacunación no"]
        print(f"Vacunación sí: {vacunado_sí} - Vacunación no: {vacunado_no}")
        if vacunado_sí:
            print("Estás vacunado...")
        else:
            print("Ya vacúnate...")
    elif event == "botón2":
        print("Click en el 2")
    