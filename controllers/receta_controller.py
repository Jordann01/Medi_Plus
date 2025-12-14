from models.receta import Receta

class RecetaController:
    def listar(self):
        return Receta.listar()

    def crear(self, id_paciente, id_medico, descripcion, medicamentos_recetados, costo_clp):
        r = Receta(id_paciente, id_medico, descripcion, medicamentos_recetados, costo_clp)
        r.guardar()
        return r

    def actualizar(self, receta: Receta):
        receta.actualizar()

    def eliminar(self, receta: Receta):
        receta.eliminar()
