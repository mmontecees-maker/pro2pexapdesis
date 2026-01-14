import os
from menus.menu_empleados import mostrar_menu_empleados
from file_manager import FileManagerEmpleado

def ejecutar_menu_empleados():
    fm = FileManagerEmpleado()
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_empleados()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n>>> REGISTRAR NUEVO EMPLEADO")
            
            # Validación de Nombre (Sin números y obligatorio)
            while True:
                nombre = input("Nombre del empleado: ").strip()
                if not nombre:
                    print("[!] Error: El nombre no puede estar vacío.")
                elif any(char.isdigit() for char in nombre):
                    print("[!] Error: El nombre no puede contener números.")
                else:
                    break
            
            # Validación de Cargo (Sin números y obligatorio)
            while True:
                cargo = input("Cargo (Terapeuta, Recepcionista, etc.): ").strip()
                if not cargo:
                    print("[!] Error: El cargo no puede estar vacío.")
                elif any(char.isdigit() for char in cargo):
                    print("[!] Error: El cargo no puede contener números.")
                else:
                    break

            fm.insert(nombre, cargo)
            print("\n[!] Empleado registrado con éxito.")
            input("Presione Enter para continuar...")

        elif opcion == "2":
            print("\n>>> LISTA DE PERSONAL")
            empleados = fm.get_all()
            if not empleados:
                print("No hay empleados registrados.")
            else:
                print(f"{'ID':<5} | {'NOMBRE':<20} | {'CARGO':<15}")
                print("-" * 45)
                for e in empleados:
                    print(f"{e['id']:<5} | {e['nombre']:<20} | {e['cargo']:<15}")
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            print("\n>>> ACTUALIZAR DATOS DE EMPLEADO")
            
            # Validación de ID (Solo números)
            while True:
                id_input = input("Ingrese el ID del empleado a editar: ").strip()
                if id_input.isdigit():
                    id_act = int(id_input)
                    break
                print("[!] Error: El ID debe ser un número entero.")

            # Verificamos si existe antes de pedir los nuevos datos
            empleados_db = {e['id']: e for e in fm.get_all()}
            if id_act in empleados_db:
                print(f"Editando a: {empleados_db[id_act]['nombre']}")
                
                # Nuevo Nombre (Validado)
                while True:
                    nuevo_nom = input("Nuevo nombre: ").strip()
                    if not nuevo_nom:
                        print("[!] Error: El campo no puede estar vacío.")
                    elif any(char.isdigit() for char in nuevo_nom):
                        print("[!] Error: No se permiten números.")
                    else:
                        break
                
                # Nuevo Cargo (Validado)
                while True:
                    nuevo_cargo = input("Nuevo cargo: ").strip()
                    if not nuevo_cargo:
                        print("[!] Error: El campo no puede estar vacío.")
                    elif any(char.isdigit() for char in nuevo_cargo):
                        print("[!] Error: No se permiten números.")
                    else:
                        break

                fm.update(id_act, nuevo_nom, nuevo_cargo)
                print("\n[!] Datos actualizados correctamente.")
            else:
                print("\n[!] Error: No se encontró el ID.")
            input("Presione Enter para continuar...")

        elif opcion == "4":
            print("\n>>> ELIMINAR EMPLEADO")
            
            # Validación de ID (Solo números)
            while True:
                id_input = input("Ingrese el ID del empleado a eliminar: ").strip()
                if id_input.isdigit():
                    id_del = int(id_input)
                    break
                print("[!] Error: Ingrese un ID numérico válido.")

            confirmar = input(f"¿Seguro que desea eliminar al empleado con ID {id_del}? (s/n): ")
            if confirmar.lower() == 's':
                if fm.delete(id_del): # Asumiendo que fm tiene el método delete
                    print("\n[!] Empleado eliminado del sistema.")
                else:
                    print("\n[!] Error: ID no encontrado.")
            else:
                print("\n[!] Operación cancelada.")
            input("Presione Enter para continuar...")

        elif opcion == "5":
            break
        else:
            print("\n[!] Opción no válida.")
            input("Presione Enter para continuar...")