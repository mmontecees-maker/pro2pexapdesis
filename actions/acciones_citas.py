import os
from menus.menu_citas import mostrar_menu_citas
from file_manager import FileManagerCita, FileManagerCliente, FileManagerEmpleado, FileManagerServicio

def ejecutar_proceso_cita():
    fm_cita = FileManagerCita()
    fm_cli = FileManagerCliente()
    fm_emp = FileManagerEmpleado()
    fm_ser = FileManagerServicio()
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_citas()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n>>> REGISTRAR NUEVA CITA")
            
            # 1. Seleccionar Cliente (Validar ID existente)
            clientes = fm_cli.get_all()
            if not clientes:
                print("[!] No hay clientes en el sistema."); input(); continue
            
            for c in clientes: print(f"[{c['id']}] {c['nombre']}")
            while True:
                id_cliente = input("ID del Cliente: ").strip()
                if id_cliente.isdigit() and any(c['id'] == int(id_cliente) for c in clientes):
                    break
                print("[!] ID no válido o inexistente.")

            # 2. Seleccionar Empleado (Validar ID existente)
            empleados = fm_emp.get_all()
            if not empleados:
                print("[!] No hay empleados en el sistema."); input(); continue
                
            for e in empleados: print(f"[{e['id']}] {e['nombre']} ({e['cargo']})")
            while True:
                id_empleado = input("ID del Terapeuta: ").strip()
                if id_empleado.isdigit() and any(e['id'] == int(id_empleado) for e in empleados):
                    break
                print("[!] ID no válido o inexistente.")

            # 3. Datos de tiempo (Validar que no estén vacíos)
            while True:
                fecha = input("Fecha (DD/MM/AAAA): ").strip()
                if fecha: break
                print("[!] La fecha es obligatoria.")
            
            while True:
                hora = input("Hora (HH:MM): ").strip()
                if hora: break
                print("[!] La hora es obligatoria.")

            # 4. Seleccionar Múltiples Servicios
            servicios_seleccionados = []
            todos_servicios = fm_ser.get_all()
            
            while True:
                print("\n--- Servicios disponibles ---")
                for s in todos_servicios: 
                    print(f"[{s['id']}] {s['nombre']} - ${s['precio']}")
                
                id_s = input("ID del servicio a agregar (o '0' para finalizar): ").strip()
                if id_s == "0": break
                
                if id_s.isdigit():
                    encontrado = next((s for s in todos_servicios if str(s['id']) == id_s), None)
                    if encontrado:
                        servicios_seleccionados.append(encontrado)
                        print(f"[✔] {encontrado['nombre']} añadido.")
                    else:
                        print("[!] ID de servicio no encontrado.")
                else:
                    print("[!] Ingrese solo el número del ID.")

            # Finalizar Registro
            if servicios_seleccionados:
                fm_cita.registrar_cita(id_cliente, id_empleado, fecha, hora, servicios_seleccionados)
                print("\n[✔] CITA AGENDADA CON ÉXITO.")
            else:
                print("\n[!] Registro cancelado: No se seleccionaron servicios.")
            input("Presione Enter para continuar...")

        elif opcion == "2":
            print("\n>>> LISTADO DE CITAS")
            citas = fm_cita.get_all_citas()
            if not citas:
                print("No hay citas registradas.")
            else:
                print(f"{'ID':<4} | {'FECHA':<10} | {'HORA':<6} | {'TOTAL':<8} | {'ESTADO'}")
                print("-" * 50)
                for c in citas:
                    # Formatear el total a moneda
                    t = float(c['total'])
                    print(f"{c['id']:<4} | {c['fecha']:<10} | {c['hora']:<6} | ${t:<7.2f} | {c['estado']}")
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            # Búsqueda de detalle de cita
            while True:
                id_v = input("ID de la cita para ver detalle (o Enter para volver): ").strip()
                if not id_v: break
                if id_v.isdigit():
                    print(f"\n>>> DETALLE DE SERVICIOS (CITA #{id_v})")
                    # Suponiendo que fm_cita tiene acceso a los detalles
                    detalles = fm_cita.get_detalles_por_cita(int(id_v))
                    if detalles:
                        for d in detalles:
                            print(f" - Servicio ID: {d['id_servicio']} | Subtotal: ${float(d['precio']):.2f}")
                        break
                    else:
                        print("[!] No se encontraron detalles para ese ID.")
                else:
                    print("[!] El ID debe ser numérico.")
            input("\nPresione Enter para continuar...")

        elif opcion == "4":
            break