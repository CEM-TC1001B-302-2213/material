import PySimpleGUI as sg

sg.theme("DarkPurple")

def crearVentanaPrincipal():
    lista_vacunas = ["Pfizer", "Cansino", "Moderna", "AstraZeneca", "Sputnik"]
    lista_spin = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]
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
                  group_id="vacunación group",
                  enable_events=True),
         sg.Radio("No estoy vacunado",
                  key="radio vacunación no",
                  group_id="vacunación group",
                  default=True,
                  enable_events=True)],
        [sg.Text("Marca de la vacuna"),
         sg.Combo(lista_vacunas,
                  key="combo vacunas",
                  default_value="Pfizer",
                  disabled=True)],
        [sg.Text("Síntomas"),
         sg.Checkbox("Fiebre", key="checkbox fiebre"),
         sg.Checkbox("Dolor de cabeza", key="checkbox dolor de cabeza"),
         sg.Checkbox("Mareos", key="checkbox mareos"),
         sg.Checkbox("Tos", key="checkbox tos")],
        [sg.Text("Nivel de satisfacción"),
         sg.Slider(range=(1,5),
                   key="slider satisfacción",
                   orientation="horizontal")],
        [sg.Text("Mes de vacunación"),
         sg.Spin(lista_spin,
                 key="spin vacunación",
                 initial_value="Marzo")],
        [sg.Image("eevee.png")]
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
        combo = values["combo vacunas"]
        print(f"Marca de la vacuna: {combo}")
        checkbox_fiebre = values["checkbox fiebre"]
        checkbox_mareos = values["checkbox mareos"]
        checkbox_dolor_cabeza = values["checkbox dolor de cabeza"]
        checkbox_tos = values["checkbox tos"]
        print(f"Fiebre: {checkbox_fiebre}")
        print(f"Mareos: {checkbox_mareos}")
        print(f"Dolor de cabeza: {checkbox_dolor_cabeza}")
        print(f"Tos: {checkbox_tos}")
        slider_satisfacción = values["slider satisfacción"]
        print(f"Nivel de satisfacción: {slider_satisfacción}")
        spin_vacunación = values["spin vacunación"]
        print(f"Mes de vacunación: {spin_vacunación}")
    elif event == "botón2":
        print("Click en el 2")
    elif event == "radio vacunación sí":
        window["combo vacunas"].update(disabled=False)
    elif event == "radio vacunación no":
        window["combo vacunas"].update(disabled=True)
    