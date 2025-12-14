from models.consulta import Consulta

class ConsultaController:
    def listar(self):
        return Consulta.listar()

    def crear(self, id_paciente, id_medico, id_receta, fecha, comentarios, valor):
        c = Consulta(id_paciente, id_medico, id_receta, fecha, comentarios, valor)
        c.guardar()
        return c

    def actualizar(self, consulta: Consulta):
        consulta.actualizar()

    def eliminar(self, consulta: Consulta):
        consulta.eliminar()
