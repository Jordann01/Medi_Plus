from models.usuario import Usuario

class AuthController:
    @staticmethod
    def login(nombre_usuario, clave):
        u = Usuario.buscar_por_nombre_usuario(nombre_usuario)
        if u and Usuario.verify_password(clave, u.clave):
            return u
        return None
