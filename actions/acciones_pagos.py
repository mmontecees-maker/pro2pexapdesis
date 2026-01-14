import os
from datetime import datetime
from menus.menu_pagos import mostrar_menu_pagos
from file_manager import FileManagerPago, FileManagerCita

def ejecutar_menu_pagos():
    fm_pago = FileManagerPago()
    fm_cita = FileManagerCita()
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_pagos()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n>>> REGISTRAR PAGO DE CITA")
            
            # 1. Obtener citas y validar que existan
            citas = fm_cita.get_all_citas()
            if not citas:
                print("[!] No hay citas registradas para cobrar.")
                input("Presione Enter para continuar...")
                continue
                
            # Listado de citas disponibles
            print(f"{'ID':<5} | {'CLIENTE':<10} | {'TOTAL':<10} | {'ESTADO'}")
            print("-" * 40)
            for c in citas:
                print(f"{c['id']:<5} | {c['id_cliente']:<10} | ${c['total']:<9} | {c['estado']}")
            
            # 2. Validar ID de Cita (Solo números)
            while True:
                id_cita_pago = input("\nIngrese el ID de la cita a pagar: ").strip()
                if id_cita_pago.isdigit():
                    break
                print("[!] Error: El ID debe ser un número entero.")
            
            # Buscar la cita para obtener el monto automáticamente
            cita_encontrada = next((c for c in citas if str(c['id']) == id_cita_pago), None)
            
            if cita_encontrada:
                monto = cita_encontrada['total']
                print(f"\n>>> Monto a cobrar: ${monto}")
                
                # 3. Validar Selección de Método de Pago
                print("Métodos: [1] Efectivo | [2] Tarjeta | [3] Transferencia")
                while True:
                    m_opc = input("Seleccione método (1-3): ").strip()
                    metodos = {"1": "Efectivo", "2": "Tarjeta", "3": "Transferencia"}
                    
                    if m_opc in metodos:
                        metodo = metodos[m_opc]
                        break
                    print("[!] Error: Seleccione una opción válida (1, 2 o 3).")
                
                fecha_hoy = datetime.now().strftime("%d/%m/%Y")
                
                # Registrar el pago
                fm_pago.registrar_pago(id_cita_pago, monto, metodo, fecha_hoy)
                
                print(f"\n[✔] Pago registrado con éxito por ${monto} via {metodo}.")
            else:
                print("\n[!] Error: El ID de cita no existe en los registros.")
            input("Presione Enter para continuar...")

        elif opcion == "2":
            print("\n>>> HISTORIAL DE PAGOS REALIZADOS")
            pagos = fm_pago.get_all()
            if not pagos:
                print("No se han registrado pagos aún.")
            else:
                print(f"{'ID':<4} | {'CITA':<5} | {'MONTO':<10} | {'MÉTODO':<15} | {'FECHA'}")
                print("-" * 55)
                for p in pagos:
                    # Formateamos el monto a 2 decimales para que se vea como dinero
                    monto_formateado = float(p['monto'])
                    print(f"{p['id']:<4} | {p['id_cita']:<5} | ${monto_formateado:<9.2f} | {p['metodo']:<15} | {p['fecha']}")
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            break
        else:
            print("\n[!] Opción inválida.")
            input("Presione Enter para continuar...")