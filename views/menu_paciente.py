from controllers.consulta_controller import ConsultaController
from controllers.receta_controller import RecetaController
from controllers.agenda_controller import AgendaController

consulta_ctrl = ConsultaController()
receta_ctrl = RecetaController()
agenda_ctrl = AgendaController()

def menu_paciente(usuario):
    while True:
        print("\n----- MENÚ PACIENTE -----")
        print("1. Ver historial de consultas")
        print("2. Ver recetas")
        print("3. Solicitar cita")
        print("4. Salir")
        opt = input("Seleccione una opción: ")
        if opt == "1":
            for c in consulta_ctrl.listar():
                if c.id_paciente == usuario.id:
                    print(f"{c.id} | Fecha: {c.fecha} | Comentarios: {c.comentarios} | Valor CLP: {c.valor}")
        elif opt == "2":
            for r in receta_ctrl.listar():
                if r.id_paciente == usuario.id:
                    print(f"{r.id} | {r.descripcion} | Medicamentos: {r.medicamentos_recetados} | Costo CLP: {r.costo_clp}")
        elif opt == "3":
            id_medico = int(input("ID médico: "))
            fecha = input("Fecha cita (YYYY-MM-DD): ")
            agenda_ctrl.crear(usuario.id, id_medico, fecha)
            print("Solicitud de cita creada (PENDIENTE).")
        elif opt == "4":
            break
        else:
            print("Opción inválida.")
