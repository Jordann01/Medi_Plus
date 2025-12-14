from models.paciente import Paciente

class PacienteController:
    def listar(self):
        return Paciente.listar()

    def crear(self, id, comuna, fecha_primera_visita=None):
        p = Paciente(id, comuna, fecha_primera_visita)
        p.guardar()
        return p

    def actualizar(self, paciente: Paciente):
        paciente.actualizar()

    def eliminar(self, paciente: Paciente):
        paciente.eliminar()
