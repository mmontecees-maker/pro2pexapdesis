import os
from menus.menu_servicios import mostrar_menu_servicios
from file_manager import FileManagerServicio

def ejecutar_menu_servicios():
    fm = FileManagerServicio()
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_servicios()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n>>> REGISTRAR NUEVO SERVICIO")
            
            # Validación de Nombre (Sin números y obligatorio)
            while True:
                nombre = input("Nombre del servicio: ").strip()
                if not nombre:
                    print("[!] Error: El nombre no puede estar vacío.")
                elif any(char.isdigit() for char in nombre):
                    print("[!] Error: El nombre no puede contener números.")
                else:
                    break
            
            # Validación de Precio (Debe ser un número positivo)
            while True:
                precio_input = input("Precio ($): ").strip()
                try:
                    precio = float(precio_input)
                    if precio >= 0:
                        break
                    print("[!] Error: El precio no puede ser negativo.")
                except ValueError:
                    print("[!] Error: Ingrese un valor numérico válido para el precio.")

            # Validación de Duración (Campo obligatorio)
            while True:
                duracion = input("Duración (ej. 60 min): ").strip()
                if duracion:
                    break
                print("[!] Error: La duración no puede estar vacía.")

            fm.insert(nombre, precio, duracion)
            print("\n[!] Servicio guardado correctamente.")
            input("Presione Enter para continuar...")

        elif opcion == "2":
            print("\n>>> LISTADO DE SERVICIOS DISPONIBLES")
            servicios = fm.get_all()
            if not servicios:
                print("No hay servicios registrados.")
            else:
                print(f"{'ID':<5} | {'SERVICIO':<25} | {'PRECIO':<10} | {'DURACIÓN'}")
                print("-" * 60)
                for s in servicios:
                    print(f"{s['id']:<5} | {s['nombre']:<25} | ${float(s['precio']):<9.2f} | {s['duracion']}")
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            print("\n>>> ACTUALIZAR SERVICIO")
            
            # Validación de ID (Solo números)
            while True:
                id_input = input("ID del servicio a editar: ").strip()
                if id_input.isdigit():
                    id_act = int(id_input)
                    break
                print("[!] Error: El ID debe ser un número entero.")

            servicios_db = {s['id']: s for s in fm.get_all()}
            
            if id_act in servicios_db:
                print(f"Editando: {servicios_db[id_act]['nombre']}")
                
                # Validación de Nuevo Nombre
                while True:
                    n_nombre = input("Nuevo nombre: ").strip()
                    if not n_nombre:
                        print("[!] Error: El nombre no puede estar vacío.")
                    elif any(char.isdigit() for char in n_nombre):
                        print("[!] Error: No se permiten números.")
                    else:
                        break
                
                # Validación de Nuevo Precio
                while True:
                    n_precio_in = input("Nuevo precio: ").strip()
                    try:
                        n_precio = float(n_precio_in)
                        if n_precio >= 0:
                            break
                        print("[!] Error: No puede ser negativo.")
                    except ValueError:
                        print("[!] Error: Ingrese un número válido.")
                
                # Validación de Nueva Duración
                while True:
                    n_duracion = input("Nueva duración: ").strip()
                    if n_duracion:
                        break
                    print("[!] Error: El campo es obligatorio.")

                # Nota: Se usa la lógica interna de tu FileManager para actualizar
                from models import Servicio
                items = fm._read_file()
                items[id_act] = Servicio(id_act, n_nombre, n_precio, n_duracion)
                fm._write_file(items)
                
                print("\n[!] Servicio actualizado correctamente.")
            else:
                print("\n[!] Error: No se encontró el ID.")
            input("Presione Enter para continuar...")

        elif opcion == "4":
            print("\n>>> ELIMINAR SERVICIO")
            
            while True:
                id_input = input("ID del servicio a eliminar: ").strip()
                if id_input.isdigit():
                    id_del = int(id_input)
                    break
                print("[!] Error: Use solo números para el ID.")

            confirmar = input(f"¿Seguro que desea eliminar el servicio {id_del}? (s/n): ")
            if confirmar.lower() == 's':
                items = fm._read_file()
                if id_del in items:
                    del items[id_del]
                    fm._write_file(items)
                    print("\n[!] Servicio eliminado.")
                else:
                    print("\n[!] Error: El ID no existe.")
            else:
                print("\n[!] Operación cancelada.")
            input("Presione Enter para continuar...")

        elif opcion == "5":
            break
        else:
            print("\n[!] Opción no válida.")
            input("Presione Enter para continuar...")