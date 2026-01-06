import os
from menus.menu_citas import mostrar_menu_citas
from file_manager import FileManagerCita, FileManagerCliente, FileManagerEmpleado, FileManagerServicio

def ejecutar_proceso_cita():
    fm_cita = FileManagerCita()
    fm_cli = FileManagerCliente()
    fm_emp = FileManagerEmpleado()
    fm_ser = FileManagerServicio()
    
    while True:
        mostrar_menu_citas()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n>>> REGISTRAR NUEVA CITA")
            
            # 1. Seleccionar Cliente
            clientes = fm_cli.get_all()
            for c in clientes: print(f"[{c['id']}] {c['nombre']}")
            id_cliente = input("ID del Cliente: ")

            # 2. Seleccionar Empleado (Terapeuta)
            empleados = fm_emp.get_all()
            for e in empleados: print(f"[{e['id']}] {e['nombre']} ({e['cargo']})")
            id_empleado = input("ID del Terapeuta: ")

            # 3. Datos de tiempo
            fecha = input("Fecha (DD/MM/AAAA): ")
            hora = input("Hora (HH:MM): ")

            # 4. Seleccionar Múltiples Servicios
            servicios_seleccionados = []
            todos_servicios = fm_ser.get_all()
            
            while True:
                print("\nServicios disponibles:")
                for s in todos_servicios: 
                    print(f"[{s['id']}] {s['nombre']} - ${s['precio']}")
                
                id_s = input("ID del servicio a agregar (o '0' para finalizar): ")
                if id_s == "0": break
                
                # Buscar el servicio en la lista
                encontrado = next((s for s in todos_servicios if str(s['id']) == id_s), None)
                if encontrado:
                    servicios_seleccionados.append(encontrado)
                    print(f"++ {encontrado['nombre']} agregado.")
                else:
                    print("[!] ID no válido.")

            if servicios_seleccionados:
                fm_cita.registrar_cita(id_cliente, id_empleado, fecha, hora, servicios_seleccionados)
                print("\n[!] CITA AGENDADA CON ÉXITO.")
            else:
                print("[!] Cita cancelada: No se seleccionaron servicios.")

        elif opcion == "2":
            print("\n>>> LISTADO DE CITAS")
            citas = fm_cita.get_all_citas()
            if not citas:
                print("No hay citas registradas.")
            else:
                print(f"{'ID':<4} | {'FECHA':<10} | {'HORA':<6} | {'TOTAL':<8} | {'ESTADO'}")
                print("-" * 50)
                for c in citas:
                    print(f"{c['id']:<4} | {c['fecha']:<10} | {c['hora']:<6} | ${c['total']:<7} | {c['estado']}")
            input("\nPresione Enter para continuar")

        elif opcion == "3":
            # Lógica para ver qué servicios hay en data/detalle_citas.txt
            id_v = input("ID de la cita para ver detalle: ")
            print(f"\n>>> DETALLE DE SERVICIOS (CITA #{id_v})")
            # Aquí podrías leer detalle_citas.txt filtrando por id_v
            # (Similar a como hacías con detalle_ventas)
            input("\nPresione Enter para continuar")

        elif opcion == "4":
            break