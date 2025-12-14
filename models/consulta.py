from models.database import Database

db = Database()

class Consulta:
    def __init__(self, id_paciente, id_medico, id_receta, fecha, comentarios, valor, id=None):
        self.id = id
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.id_receta = id_receta
        self.fecha = fecha
        self.comentarios = comentarios
        self.valor = valor  # CLP

    def guardar(self):
        try:
            c = db.cursor()
            fecha = self.fecha
            if isinstance(fecha, str):
                c.execute("INSERT INTO consultas (id_paciente, id_medico, id_receta, fecha, comentarios, valor) VALUES (:1,:2,:3, TO_DATE(:4,'YYYY-MM-DD'),:5,:6)",
                          (self.id_paciente, self.id_medico, self.id_receta, fecha, self.comentarios, self.valor))
            else:
                c.execute("INSERT INTO consultas (id_paciente, id_medico, id_receta, fecha, comentarios, valor) VALUES (:1,:2,:3,:4,:5,:6)",
                          (self.id_paciente, self.id_medico, self.id_receta, fecha, self.comentarios, self.valor))
            db.commit()
        except Exception as e:
            print("Error al guardar consulta:", e)

    @staticmethod
    def listar():
        try:
            c = db.cursor()
            c.execute("SELECT id, id_paciente, id_medico, id_receta, fecha, comentarios, valor FROM consultas")
            res = []
            for fila in c.fetchall():
                fecha = fila[4].strftime("%Y-%m-%d") if fila[4] else None
                res.append(Consulta(fila[1], fila[2], fila[3], fecha, fila[5], float(fila[6]) if fila[6] is not None else 0.0, id=fila[0]))
            return res
        except Exception as e:
            print("Error al listar consultas:", e)
            return []

    def actualizar(self):
        try:
            c = db.cursor()
            fecha = self.fecha
            if isinstance(fecha, str):
                c.execute("UPDATE consultas SET id_paciente=:1, id_medico=:2, id_receta=:3, fecha=TO_DATE(:4,'YYYY-MM-DD'), comentarios=:5, valor=:6 WHERE id=:7",
                          (self.id_paciente, self.id_medico, self.id_receta, fecha, self.comentarios, self.valor, self.id))
            else:
                c.execute("UPDATE consultas SET id_paciente=:1, id_medico=:2, id_receta=:3, fecha=:4, comentarios=:5, valor=:6 WHERE id=:7",
                          (self.id_paciente, self.id_medico, self.id_receta, fecha, self.comentarios, self.valor, self.id))
            db.commit()
        except Exception as e:
            print("Error al actualizar consulta:", e)

    def eliminar(self):
        try:
            c = db.cursor()
            c.execute("DELETE FROM consultas WHERE id=:1", (self.id,))
            db.commit()
        except Exception as e:
            print("Error al eliminar consulta:", e)

    def valor_usd(self):
        from config import USD_TO_CLP
        return (self.valor or 0.0) / USD_TO_CLP
