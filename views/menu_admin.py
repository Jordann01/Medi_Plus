from controllers.usuario_controller import UsuarioController
from controllers.insumo_controller import InsumoController
from controllers.consulta_controller import ConsultaController
from controllers.receta_controller import RecetaController
from controllers.paciente_controller import PacienteController
from controllers.medico_controller import MedicoController

usuario_ctrl = UsuarioController()
insumo_ctrl = InsumoController()
consulta_ctrl = ConsultaController()
receta_ctrl = RecetaController()
paciente_ctrl = PacienteController()
medico_ctrl = MedicoController()

def menu_administrador():
    while True:
        print("\n--- MENÚ ADMINISTRADOR ---")
        print("1. Usuarios")
        print("2. Pacientes")
        print("3. Médicos")
        print("4. Insumos")
        print("5. Consultas")
        print("6. Recetas")
        print("0. Salir")
        
        opt = input("Opción: ").strip()

        if opt == "1":
            usuarios = usuario_ctrl.listar()
            for u in usuarios:
                print(f"{u.id} | {u.nombre_usuario} | {u.nombre} {u.apellido} | {u.tipo}")

        elif opt == "2":
            pacientes = paciente_ctrl.listar()
            for p in pacientes:
                print(f"{p.id} | {p.comuna} | {p.fecha_primera_visita}")

        elif opt == "3":
            medicos = medico_ctrl.listar()
            for m in medicos:
                print(f"{m.id} | {m.especialidad} | {m.horario_atencion} | {m.fecha_ingreso}")
