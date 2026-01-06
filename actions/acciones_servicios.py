import os
from menus.menu_servicios import mostrar_menu_servicios
from file_manager import FileManagerServicio

def ejecutar_menu_servicios():
    fm = FileManagerServicio()
    
    while True:
        mostrar_menu_servicios()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n>>> REGISTRAR NUEVO SERVICIO")
            nombre = input("Nombre del servicio (ej. Masaje Sueco): ")
            try:
                precio = float(input("Precio ($): "))
                duracion = input("Duración (ej. 60 min): ")
                fm.insert(nombre, precio, duracion)
                print("[!] Servicio guardado correctamente.")
            except ValueError:
                print("[!] Error: El precio debe ser un número.")

        elif opcion == "2":
            print("\n>>> LISTADO DE SERVICIOS DISPONIBLES")
            servicios = fm.get_all()
            if not servicios:
                print("No hay servicios registrados.")
            else:
                print(f"{'ID':<5} | {'SERVICIO':<25} | {'PRECIO':<10} | {'DURACIÓN'}")
                print("-" * 60)
                for s in servicios:
                    print(f"{s['id']:<5} | {s['nombre']:<25} | ${s['precio']:<9} | {s['duracion']}")
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            print("\n>>> ACTUALIZAR SERVICIO")
            try:
                id_act = int(input("ID del servicio a editar: "))
                nombre = input("Nuevo nombre: ")
                precio = float(input("Nuevo precio: "))
                duracion = input("Nueva duración: ")
                
                # Reutilizamos la lógica de escritura del FileManager
                items = fm._read_file()
                if id_act in items:
                    from models import Servicio
                    items[id_act] = Servicio(id_act, nombre, precio, duracion)
                    fm._write_file(items)
                    print("[!] Servicio actualizado.")
                else:
                    print("[!] Error: ID no encontrado.")
            except ValueError:
                print("[!] Error: Datos inválidos.")

        elif opcion == "4":
            print("\n>>> ELIMINAR SERVICIO")
            try:
                id_del = int(input("ID del servicio a eliminar: "))
                items = fm._read_file()
                if id_del in items:
                    del items[id_del]
                    fm._write_file(items)
                    print("[!] Servicio eliminado.")
                else:
                    print("[!] Error: ID no encontrado.")
            except ValueError:
                print("[!] Error: ID inválido.")

        elif opcion == "5":
            break
        else:
            print("Opción inválida.")