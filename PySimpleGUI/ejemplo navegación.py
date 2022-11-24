import PySimpleGUI as sg

def crearVentanaIniciarSesion():
    col1 = sg.Column([
        [sg.Text("Usuario")],
        [sg.Text("Contraseña")]
        ])
    col2 = sg.Column([
        [sg.Input(key="iniciar sesión input usuario")],
        [sg.Input(key="iniciar sesión input contraseña", password_char="*")]
        ])
    layout = [
        [col1, col2],
        [sg.Button("Iniciar sesión", key="iniciar sesión botón iniciar"),
         sg.Button("Registrarse", key="iniciar sesión botón registrar")]
        ]
    return sg.Window("Inicio de sesión", layout, finalize=True)

def crearVentanaRegistro():
    col1 = sg.Column([
        [sg.Text("Usuario")],
        [sg.Text("Contraseña")],
        [sg.Text("Repetir contraseña")],
        [sg.Text("Recibir notificaciones")]
        ])
    col2 = sg.Column([
        [sg.Input(key="registro input usuario")],
        [sg.Input(key="registro input contraseña", password_char="*")],
        [sg.Input(key="registro input repetir contraseña", password_char="*")],
        [sg.Radio("Sí", key="registro radio sí", group_id="registro grupo"),
         sg.Radio("No", key="registro radio no", group_id="registro grupo")]
        ])
    layout = [
        [col1, col2],
        [sg.Button("Registrarse", key="registro botón registrar"),
         sg.Button("Volver", key="registro botón volver")]
        ]
    return sg.Window("Registro", layout, finalize=True)

def crearVentanaMenuPrincipal():
    layout = [
        [sg.Text("Menú principal")],
        [sg.Button("Mapa", key="menú principal mapa")],
        [sg.Button("Salir", key="menú principal salir")]
        ]
    return sg.Window("Menú principal", layout, finalize=True)

ventanaIniciarSesion = crearVentanaIniciarSesion()
ventanaRegistro = None
ventanaMenuPrincipal = None

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED or event == "menú principal salir":
        window.close()
        break
    # ¿En qué ventana estoy?
    # ¿Qué botón se oprimió?
    # ¿La ventana hacia donde voy estaba cerrada?
    # Iniciar Sesión -> Registro
    elif window == ventanaIniciarSesion and event == "iniciar sesión botón registrar" and ventanaRegistro is None:
        # Cerrar la ventana actual
        window.close()
        # Poner en None la variable de mi ventana actual
        ventanaIniciarSesion = None
        # Abrir la nueva ventana y ponerla en su variable
        ventanaRegistro = crearVentanaRegistro()
    # Iniciar Sesión -> Menú Principal
    elif window == ventanaIniciarSesion and event == "iniciar sesión botón iniciar" and ventanaMenuPrincipal is None:
        usuario = values["iniciar sesión input usuario"]
        contraseña = values["iniciar sesión input contraseña"]
        if usuario == "aram" and contraseña == "pass":
            window.close()
            ventanaIniciarSesion = None
            ventanaMenuPrincipal = crearVentanaMenuPrincipal()
        else:
            sg.Popup("Los datos son incorrectos", title="Error")
    # Registro -> Menú Principal
    elif window == ventanaRegistro and event == "registro botón registrar" and ventanaMenuPrincipal is None:
        contraseña = values["registro input contraseña"]
        repetir_contraseña = values["registro input repetir contraseña"]
        if contraseña == repetir_contraseña and contraseña != "":
            window.close()
            ventanaRegistro = None
            ventanaMenuPrincipal = crearVentanaMenuPrincipal()
        else:
            sg.Popup("Las contraseñas no coinciden o están vacias.", title="Error")
    # Registro -> Iniciar sesión
    elif window == ventanaRegistro and event == "registro botón volver" and ventanaIniciarSesion is None:
        window.close()
        ventanaRegistro = None
        ventanaIniciarSesion = crearVentanaIniciarSesion()