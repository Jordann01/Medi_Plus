from models.medico import Medico

class MedicoController:
    def listar(self):
        return Medico.listar()

    def crear(self, id, especialidad, horario_atencion, fecha_ingreso=None):
        m = Medico(id, especialidad, horario_atencion, fecha_ingreso)
        m.guardar()
        return m

    def actualizar(self, medico: Medico):
        medico.actualizar()

    def eliminar(self, medico: Medico):
        medico.eliminar()

