from controllers.consulta_controller import ConsultaController
from controllers.receta_controller import RecetaController

consulta_ctrl = ConsultaController()
receta_ctrl = RecetaController()

def menu_medico(usuario):
    while True:
        print("\n----- MENÚ MÉDICO -----")
        print("1. Registrar Consulta")
        print("2. Registrar Receta")
        print("3. Salir")

        opt = input("Seleccione una opción: ").strip()

        if opt == "1":
            id_paciente = int(input("ID paciente: "))
            id_receta = input("ID receta (o dejar en blanco): ")
            id_receta = int(id_receta) if id_receta else None

            fecha = input("Fecha (YYYY-MM-DD): ")
            comentarios = input("Comentarios: ")
            valor = float(input("Valor CLP: "))

            consulta_ctrl.crear(id_paciente, usuario.id, id_receta, fecha, comentarios, valor)
            print("Consulta registrada correctamente.")

        elif opt == "2":
            id_paciente = int(input("ID paciente: "))
            descripcion = input("Descripción: ")
            medicamentos = input("Medicamentos recetados: ")
            costo = float(input("Costo CLP: "))

            receta_ctrl.crear(id_paciente, usuario.id, descripcion, medicamentos, costo)
            print("Receta creada correctamente.")

        elif opt == "3":
            break

        else:
            print("Opción inválida.")
