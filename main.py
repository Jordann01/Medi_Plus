from controllers.json_loader import cargar_usuarios_desde_json
from views.login_view import login_prompt
from views.menu_admin import menu_administrador
from views.menu_medico import menu_medico
from views.menu_paciente import menu_paciente

if __name__ == "__main__":
    # carga inicial desde JSON (si no existen usuarios)
    cargar_usuarios_desde_json()
    usuario = None
    while usuario is None:
        usuario = login_prompt()
    tipo = usuario.tipo.upper() if usuario.tipo else ""
    if tipo in ("ADMIN", "ADMINISTRADOR"):
        menu_administrador()
    elif tipo == "MEDICO":
        menu_medico(usuario)
    elif tipo == "PACIENTE":
        menu_paciente(usuario)
    else:
        print("Tipo de usuario no reconocido.")
