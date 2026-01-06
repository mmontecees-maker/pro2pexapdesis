import os
from menus.menu_empleados import mostrar_menu_empleados
from file_manager import FileManagerEmpleado

def ejecutar_menu_empleados():
    fm = FileManagerEmpleado()
    
    while True:
        mostrar_menu_empleados()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n>>> REGISTRAR NUEVO EMPLEADO")
            nombre = input("Nombre del empleado: ")
            cargo = input("Cargo (Terapeuta, Recepcionista, etc.): ")
            fm.insert(nombre, cargo)
            print("[!] Empleado registrado con éxito.")

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
            try:
                id_act = int(input("Ingrese el ID del empleado a editar: "))
                nombre = input("Nuevo nombre: ")
                cargo = input("Nuevo cargo: ")
                if fm.update(id_act, nombre, cargo):
                    print("[!] Datos actualizados correctamente.")
                else:
                    print("[!] Error: No se encontró el ID.")
            except ValueError:
                print("[!] Error: Ingrese un ID numérico válido.")

        elif opcion == "4":
            print("\n>>> ELIMINAR EMPLEADO")
            try:
                # Nota: Tu FileManagerEmpleado necesita el método delete. 
                # Si no lo tienes, puedes agregarlo igual que en Clientes.
                id_del = int(input("Ingrese el ID del empleado a eliminar: "))
                confirmar = input(f"¿Seguro que desea eliminar al empleado con ID {id_del}? (s/n): ")
                if confirmar.lower() == 's':
                    # Usamos la lógica de delete heredada o implementada
                    items = fm._read_file()
                    if id_del in items:
                        del items[id_del]
                        fm._write_file(items)
                        print("[!] Empleado eliminado del sistema.")
                    else:
                        print("[!] Error: ID no encontrado.")
            except ValueError:
                print("[!] Error: ID inválido.")

        elif opcion == "5":
            break
        else:
            print("Opción no válida.")