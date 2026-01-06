import os
from menus.menu_clientes import mostrar_menu_clientes
from file_manager import FileManagerCliente

def ejecutar_menu_clientes():
    fm = FileManagerCliente()
    
    while True:
        mostrar_menu_clientes()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n>>> REGISTRAR NUEVO CLIENTE")
            nombre = input("Nombre completo: ")
            ruc = input("RUC/DNI: ")
            telefono = input("Teléfono: ")
            fm.insert(nombre, ruc, telefono)
            print("[!] Cliente registrado con éxito.")

        elif opcion == "2":
            print("\n>>> LISTA DE CLIENTES")
            clientes = fm.get_all()
            if not clientes:
                print("No hay clientes registrados.")
            else:
                for c in clientes:
                    print(f"ID: {c['id']} | Nombre: {c['nombre']} | RUC: {c['ruc']} | Tel: {c['telefono']}")
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            print("\n>>> ACTUALIZAR CLIENTE")
            id_act = int(input("Ingrese el ID del cliente a editar: "))
            nombre = input("Nuevo nombre: ")
            ruc = input("Nuevo RUC: ")
            telefono = input("Nuevo teléfono: ")
            if fm.update(id_act, nombre, ruc, telefono):
                print("[!] Cliente actualizado correctamente.")
            else:
                print("[!] Error: No se encontró el ID.")

        elif opcion == "4":
            print("\n>>> ELIMINAR CLIENTE")
            id_del = int(input("Ingrese el ID del cliente a eliminar: "))
            confirmar = input(f"¿Seguro que desea eliminar al ID {id_del}? (s/n): ")
            if confirmar.lower() == 's':
                if fm.delete(id_del):
                    print("[!] Cliente eliminado.")
                else:
                    print("[!] Error: No se encontró el ID.")

        elif opcion == "5":
            break
        else:
            print("Opción no válida.")