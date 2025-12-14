from models.database import Database
from config import USD_TO_CLP

db = Database()

class Receta:
    def __init__(self, id_paciente, id_medico, descripcion, medicamentos_recetados, costo_clp, id=None):
        self.id = id
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.descripcion = descripcion
        self.medicamentos_recetados = medicamentos_recetados
        self.costo_clp = costo_clp

    def guardar(self):
        try:
            c = db.cursor()
            c.execute(
                "INSERT INTO RECETA (id_paciente, id_medico, descripcion, medicamentos_recetados, costo_clp) "
                "VALUES (:1,:2,:3,:4,:5)",
                (self.id_paciente, self.id_medico, self.descripcion, self.medicamentos_recetados, self.costo_clp)
            )
            db.conectar().commit()
            print("Receta guardada correctamente.")
        except Exception as e:
            print("Error al guardar receta:", e)

    @staticmethod
    def listar():
        try:
            c = db.cursor()
            c.execute("SELECT id, id_paciente, id_medico, descripcion, medicamentos_recetados, costo_clp FROM RECETA")
            recetas = []
            for fila in c.fetchall():
                recetas.append(Receta(*fila[1:], id=fila[0]))
            return recetas
        except Exception as e:
            print("Error al listar recetas:", e)
            return []

    def actualizar(self):
        try:
            c = db.cursor()
            c.execute(
                "UPDATE RECETA SET id_paciente=:1, id_medico=:2, descripcion=:3, medicamentos_recetados=:4, costo_clp=:5 "
                "WHERE id=:6",
                (self.id_paciente, self.id_medico, self.descripcion, self.medicamentos_recetados, self.costo_clp, self.id)
            )
            db.conectar().commit()
            print("Receta actualizada correctamente.")
        except Exception as e:
            print("Error al actualizar receta:", e)

    def eliminar(self):
        try:
            c = db.cursor()
            c.execute("DELETE FROM RECETA WHERE id=:1", (self.id,))
            db.conectar().commit()
            print("Receta eliminada correctamente.")
        except Exception as e:
            print("Error al eliminar receta:", e)

    def costo_usd(self):
        """Convierte el costo de CLP a USD usando la tasa definida"""
        return self.costo_clp / USD_TO_CLP
