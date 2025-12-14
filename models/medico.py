from models.database import Database
from datetime import datetime

db = Database()

class Medico:
    def __init__(self, id, especialidad, horario_atencion, fecha_ingreso=None):
        self.id = id
        self.especialidad = especialidad
        self.horario_atencion = horario_atencion
        self.fecha_ingreso = fecha_ingreso

    def guardar(self):
        try:
            c = db.cursor()
            fecha = self.fecha_ingreso
            if isinstance(fecha, str):
                c.execute("INSERT INTO medicos (id, especialidad, horario_atencion, fecha_ingreso) VALUES (:1,:2,:3, TO_DATE(:4,'YYYY-MM-DD'))",
                          (self.id, self.especialidad, self.horario_atencion, fecha))
            else:
                c.execute("INSERT INTO medicos (id, especialidad, horario_atencion, fecha_ingreso) VALUES (:1,:2,:3,:4)",
                          (self.id, self.especialidad, self.horario_atencion, fecha))
            db.commit()
        except Exception as e:
            print("Error al guardar medico:", e)

    @staticmethod
    def listar():
        try:
            c = db.cursor()
            c.execute("SELECT id, especialidad, horario_atencion, fecha_ingreso FROM medicos")
            res = []
            for fila in c.fetchall():
                fecha = fila[3].strftime("%Y-%m-%d") if fila[3] else None
                res.append(Medico(fila[0], fila[1], fila[2], fecha))
            return res
        except Exception as e:
            print("Error al listar medicos:", e)
            return []

    def actualizar(self):
        try:
            c = db.cursor()
            fecha = self.fecha_ingreso
            if isinstance(fecha, str):
                c.execute("UPDATE medicos SET especialidad=:1, horario_atencion=:2, fecha_ingreso=TO_DATE(:3,'YYYY-MM-DD') WHERE id=:4",
                          (self.especialidad, self.horario_atencion, fecha, self.id))
            else:
                c.execute("UPDATE medicos SET especialidad=:1, horario_atencion=:2, fecha_ingreso=:3 WHERE id=:4",
                          (self.especialidad, self.horario_atencion, fecha, self.id))
            db.commit()
        except Exception as e:
            print("Error al actualizar medico:", e)

    def eliminar(self):
        try:
            c = db.cursor()
            c.execute("DELETE FROM medicos WHERE id=:1", (self.id,))
            db.commit()
        except Exception as e:
            print("Error al eliminar medico:", e)
