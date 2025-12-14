from models.database import Database
from datetime import datetime

db = Database()

class Paciente:
    def __init__(self, id, comuna, fecha_primera_visita=None):
        self.id = id
        self.comuna = comuna
        self.fecha_primera_visita = fecha_primera_visita

    def guardar(self):
        try:
            c = db.cursor()
            fecha = self.fecha_primera_visita
            if isinstance(fecha, str):
                c.execute("INSERT INTO pacientes (id, comuna, fecha_primera_visita) VALUES (:1,:2, TO_DATE(:3,'YYYY-MM-DD'))",
                          (self.id, self.comuna, fecha))
            else:
                c.execute("INSERT INTO pacientes (id, comuna, fecha_primera_visita) VALUES (:1,:2,:3)",
                          (self.id, self.comuna, fecha))
            db.commit()
        except Exception as e:
            print("Error al guardar paciente:", e)

    @staticmethod
    def listar():
        try:
            c = db.cursor()
            c.execute("SELECT id, comuna, fecha_primera_visita FROM pacientes")
            res = []
            for fila in c.fetchall():
                fecha = fila[2].strftime("%Y-%m-%d") if fila[2] else None
                res.append(Paciente(fila[0], fila[1], fecha))
            return res
        except Exception as e:
            print("Error al listar pacientes:", e)
            return []

    def actualizar(self):
        try:
            c = db.cursor()
            fecha = self.fecha_primera_visita
            if isinstance(fecha, str):
                c.execute("UPDATE pacientes SET comuna=:1, fecha_primera_visita=TO_DATE(:2,'YYYY-MM-DD') WHERE id=:3",
                          (self.comuna, fecha, self.id))
            else:
                c.execute("UPDATE pacientes SET comuna=:1, fecha_primera_visita=:2 WHERE id=:3",
                          (self.comuna, fecha, self.id))
            db.commit()
        except Exception as e:
            print("Error al actualizar paciente:", e)

    def eliminar(self):
        try:
            c = db.cursor()
            c.execute("DELETE FROM pacientes WHERE id=:1", (self.id,))
            db.commit()
        except Exception as e:
            print("Error al eliminar paciente:", e)
