from models.usuario import Usuario

class UsuarioController:
    def listar(self):
        return Usuario.listar()

    def crear(self, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo):
        u = Usuario(nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo)
        u.guardar()
        return u

    def actualizar(self, usuario: Usuario):
        usuario.actualizar()

    def eliminar(self, usuario: Usuario):
        usuario.eliminar()
