import json, os
from config import get_dsn
from config import ORACLE_USER, ORACLE_PASSWORD, ORACLE_DSN
from models.usuario import Usuario

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "usuarios.json")

def cargar_usuarios_desde_json(ruta=None):
    ruta = ruta or DATA_PATH
    if not os.path.exists(ruta):
        return
    with open(ruta, "r", encoding="utf-8") as f:
        datos = json.load(f)
    for u in datos.get("usuarios", []):
        existing = Usuario.buscar_por_nombre_usuario(u.get("nombre_usuario"))
        if existing:
            continue
        usuario = Usuario(
            nombre_usuario=u.get("nombre_usuario"),
            clave=u.get("clave"),
            nombre=u.get("nombre"),
            apellido=u.get("apellido"),
            fecha_nacimiento=u.get("fecha_nacimiento"),
            telefono=u.get("telefono"),
            email=u.get("email"),
            tipo=u.get("tipo")
        )
        usuario.guardar()
