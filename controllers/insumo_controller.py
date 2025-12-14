from models.insumo import Insumo

class InsumoController:
    def listar(self):
        return Insumo.listar()

    def crear(self, nombre, tipo, stock, costo_usd):
        i = Insumo(nombre, tipo, stock, costo_usd)
        i.guardar()
        return i

    def actualizar(self, insumo: Insumo):
        insumo.actualizar()

    def eliminar(self, insumo: Insumo):
        insumo.eliminar()
