from models.database import Database
from config import USD_TO_CLP

db = Database()

class Insumo:
    def __init__(self, nombre, tipo, stock, costo_usd, id=None):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.stock = stock
        self.costo_usd = costo_usd

    def guardar(self):
        try:
            c = db.cursor()
            c.execute("INSERT INTO insumos (nombre, tipo, stock, costo_usd) VALUES (:1,:2,:3,:4)",
                      (self.nombre, self.tipo, self.stock, self.costo_usd))
            db.commit()
        except Exception as e:
            print("Error al guardar insumo:", e)

    @staticmethod
    def listar():
        try:
            c = db.cursor()
            c.execute("SELECT id, nombre, tipo, stock, costo_usd FROM insumos")
            res = []
            for fila in c.fetchall():
                res.append(Insumo(fila[1], fila[2], fila[3], float(fila[4]) if fila[4] is not None else 0.0, id=fila[0]))
            return res
        except Exception as e:
            print("Error al listar insumos:", e)
            return []

    def actualizar(self):
        try:
            c = db.cursor()
            c.execute("UPDATE insumos SET nombre=:1, tipo=:2, stock=:3, costo_usd=:4 WHERE id=:5",
                      (self.nombre, self.tipo, self.stock, self.costo_usd, self.id))
            db.commit()
        except Exception as e:
            print("Error al actualizar insumo:", e)

    def eliminar(self):
        try:
            c = db.cursor()
            c.execute("DELETE FROM insumos WHERE id=:1", (self.id,))
            db.commit()
        except Exception as e:
            print("Error al eliminar insumo:", e)

    def costo_clp(self):
        return (self.costo_usd or 0.0) * USD_TO_CLP
