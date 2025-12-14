from models.database import Database

db = Database()

class Agenda:
    def __init__(self, id_paciente, id_medico, fecha_consulta, estado="PENDIENTE", id=None):
        self.id = id
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.fecha_consulta = fecha_consulta
        self.estado = estado

    def guardar(self):
        try:
            c = db.cursor()
            fecha = self.fecha_consulta
            if isinstance(fecha, str):
                c.execute("INSERT INTO agenda (id_paciente, id_medico, fecha_consulta, estado) VALUES (:1,:2, TO_DATE(:3,'YYYY-MM-DD'), :4)",
                          (self.id_paciente, self.id_medico, fecha, self.estado))
            else:
                c.execute("INSERT INTO agenda (id_paciente, id_medico, fecha_consulta, estado) VALUES (:1,:2,:3,:4)",
                          (self.id_paciente, self.id_medico, fecha, self.estado))
            db.commit()
        except Exception as e:
            print("Error al guardar cita:", e)

    @staticmethod
    def listar():
        try:
            c = db.cursor()
            c.execute("SELECT id, id_paciente, id_medico, fecha_consulta, estado FROM agenda")
            res = []
            for fila in c.fetchall():
                fecha = fila[3].strftime("%Y-%m-%d") if fila[3] else None
                res.append(Agenda(fila[1], fila[2], fecha, fila[4], id=fila[0]))
            return res
        except Exception as e:
            print("Error al listar agenda:", e)
            return []

    def actualizar(self):
        try:
            c = db.cursor()
            fecha = self.fecha_consulta
            if isinstance(fecha, str):
                c.execute("UPDATE agenda SET id_paciente=:1, id_medico=:2, fecha_consulta=TO_DATE(:3,'YYYY-MM-DD'), estado=:4 WHERE id=:5",
                          (self.id_paciente, self.id_medico, fecha, self.estado, self.id))
            else:
                c.execute("UPDATE agenda SET id_paciente=:1, id_medico=:2, fecha_consulta=:3, estado=:4 WHERE id=:5",
                          (self.id_paciente, self.id_medico, fecha, self.estado, self.id))
            db.commit()
        except Exception as e:
            print("Error al actualizar cita:", e)

    def eliminar(self):
        try:
            c = db.cursor()
            c.execute("DELETE FROM agenda WHERE id=:1", (self.id,))
            db.commit()
        except Exception as e:
            print("Error al eliminar cita:", e)
