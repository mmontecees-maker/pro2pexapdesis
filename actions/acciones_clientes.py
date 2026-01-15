import os
from menus.menu_clientes import mostrar_menu_clientes
from file_manager import FileManagerCliente

def ejecutar_menu_clientes():
    fm = FileManagerCliente()
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_clientes()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n>>> REGISTRAR NUEVO CLIENTE")
            
            # Validación de Nombre (Sin números y obligatorio)
            while True:
                nombre = input("Nombre del cliente: ").strip()
                if not nombre:
                    print("[!] Error: El nombre no puede estar vacío.")
                elif any(char.isdigit() for char in nombre):
                    print("[!] Error: El nombre no puede contener números.")
                else:
                    break
            
            # Validación de RUC (Solo números y obligatorio)
            while True:
                ruc = input("RUC del cliente: ").strip()
                if not ruc:
                    print("[!] Error: El RUC no puede estar vacío.")
                elif not ruc.isdigit():
                    print("[!] Error: El RUC solo puede contener números.")
                else:
                    break
            
            # Validación de Teléfono (Solo números y obligatorio)
            while True:
                telefono = input("Teléfono del cliente: ").strip()
                if not telefono:
                    print("[!] Error: El teléfono no puede estar vacío.")
                elif not telefono.isdigit():
                    print("[!] Error: El teléfono solo puede contener números.")
                else:
                    break

            fm.insert(nombre, ruc, telefono)
            print("\n[!] Cliente registrado con éxito.")
            input("Presione Enter para continuar...")

        elif opcion == "2":
            print("\n>>> LISTA DE CLIENTES")
            clientes = fm.get_all()
            if not clientes:
                print("No hay clientes registrados.")
            else:
                print(f"{'ID':<5} | {'NOMBRE':<20} | {'RUC':<12} | {'TELÉFONO':<12}")
                print("-" * 55)
                for c in clientes:
                    print(f"{c['id']:<5} | {c['nombre']:<20} | {c['ruc']:<12} | {c['telefono']:<12}")
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            print("\n>>> ACTUALIZAR DATOS DE CLIENTE")
            
            # Validación de ID (Solo números)
            while True:
                id_input = input("Ingrese el ID del cliente a editar: ").strip()
                if id_input.isdigit():
                    id_act = int(id_input)
                    break
                print("[!] Error: El ID debe ser un número entero.")

            # Verificamos si existe antes de pedir los nuevos datos
            clientes_db = {c['id']: c for c in fm.get_all()}
            if id_act in clientes_db:
                print(f"Editando a: {clientes_db[id_act]['nombre']}")
                
                # Nuevo Nombre (Validado)
                while True:
                    nuevo_nom = input("Nuevo nombre: ").strip()
                    if not nuevo_nom:
                        print("[!] Error: El campo no puede estar vacío.")
                    elif any(char.isdigit() for char in nuevo_nom):
                        print("[!] Error: No se permiten números.")
                    else:
                        break
                
                # Nuevo RUC (Validado)
                while True:
                    nuevo_ruc = input("Nuevo RUC: ").strip()
                    if not nuevo_ruc:
                        print("[!] Error: El campo no puede estar vacío.")
                    elif not nuevo_ruc.isdigit():
                        print("[!] Error: El RUC solo puede contener números.")
                    else:
                        break
                
                # Nuevo Teléfono (Validado)
                while True:
                    nuevo_tel = input("Nuevo teléfono: ").strip()
                    if not nuevo_tel:
                        print("[!] Error: El campo no puede estar vacío.")
                    elif not nuevo_tel.isdigit():
                        print("[!] Error: El teléfono solo puede contener números.")
                    else:
                        break

                fm.update(id_act, nuevo_nom, nuevo_ruc, nuevo_tel)
                print("\n[!] Datos actualizados correctamente.")
            else:
                print("\n[!] Error: No se encontró el ID.")
            input("Presione Enter para continuar...")

        elif opcion == "4":
            print("\n>>> ELIMINAR CLIENTE")
            
            # Validación de ID (Solo números)
            while True:
                id_input = input("Ingrese el ID del cliente a eliminar: ").strip()
                if id_input.isdigit():
                    id_del = int(id_input)
                    break
                print("[!] Error: Ingrese un ID numérico válido.")

            confirmar = input(f"¿Seguro que desea eliminar al cliente con ID {id_del}? (s/n): ")
            if confirmar.lower() == 's':
                if fm.delete(id_del):
                    print("\n[!] Cliente eliminado del sistema.")
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
