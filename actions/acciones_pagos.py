import os
from datetime import datetime
from menus.menu_pagos import mostrar_menu_pagos
from file_manager import FileManagerPago, FileManagerCita

def ejecutar_menu_pagos():
    fm_pago = FileManagerPago()
    fm_cita = FileManagerCita()
    
    while True:
        mostrar_menu_pagos()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n>>> REGISTRAR PAGO DE CITA")
            
            # 1. Mostrar citas para saber cuál pagar
            citas = fm_cita.get_all_citas()
            if not citas:
                print("No hay citas registradas para cobrar.")
                continue
                
            print(f"{'ID':<5} | {'CLIENTE':<10} | {'TOTAL':<10} | {'ESTADO'}")
            for c in citas:
                print(f"{c['id']:<5} | {c['id_cliente']:<10} | ${c['total']:<9} | {c['estado']}")
            
            id_cita_pago = input("\nIngrese el ID de la cita a pagar: ")
            
            # Buscar la cita para obtener el monto automáticamente
            cita_encontrada = next((c for c in citas if str(c['id']) == id_cita_pago), None)
            
            if cita_encontrada:
                monto = cita_encontrada['total']
                print(f"Monto a cobrar: ${monto}")
                
                print("Métodos: [1] Efectivo | [2] Tarjeta | [3] Transferencia")
                m_opc = input("Seleccione método: ")
                metodos = {"1": "Efectivo", "2": "Tarjeta", "3": "Transferencia"}
                metodo = metodos.get(m_opc, "Otro")
                
                fecha_hoy = datetime.now().strftime("%d/%m/%Y")
                
                # Registrar el pago
                fm_pago.registrar_pago(id_cita_pago, monto, metodo, fecha_hoy)
                
                # Opcional: Podrías actualizar el estado de la cita a "Pagada" aquí
                print(f"\n[!] Pago registrado con éxito por ${monto} via {metodo}.")
            else:
                print("[!] ID de cita no encontrado.")

        elif opcion == "2":
            print("\n>>> HISTORIAL DE PAGOS REALIZADOS")
            pagos = fm_pago.get_all()
            if not pagos:
                print("No se han registrado pagos aún.")
            else:
                print(f"{'ID':<4} | {'CITA':<5} | {'MONTO':<10} | {'MÉTODO':<15} | {'FECHA'}")
                print("-" * 55)
                for p in pagos:
                    print(f"{p['id']:<4} | {p['id_cita']:<5} | ${p['monto']:<9} | {p['metodo']:<15} | {p['fecha']}")
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            break
        else:
            print("Opción inválida.")