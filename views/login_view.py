import getpass
from controllers.auth_controller import AuthController
from views.menu_admin import menu_administrador
from views.menu_medico import menu_medico
from views.menu_paciente import menu_paciente

def login_prompt():
    print("----- LOGIN -----")
    nombre_usuario = input("Usuario: ").strip()
    clave = getpass.getpass("Contraseña: ")
    user = AuthController.login(nombre_usuario, clave)
    if user:
        print(f"Bienvenido {user.nombre} ({user.tipo})")
    else:
        print("Usuario o contraseña incorrecta")
    return user
