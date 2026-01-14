import os
from file_manager import FileManagerPago

def ejecutar_reportes_spa():
    fm_p = FileManagerPago()
    
    # Limpiar pantalla al entrar
    os.system("cls" if os.name == "nt" else "clear")
    
    print("\n" + "═"*35)
    print("       REPORTE FINANCIERO SPA")
    print("" + "═"*35)
    
    # Obtener todos los pagos registrados
    pagos = fm_p.get_all()
    
    if not pagos:
        print("\n[!] No se han encontrado registros de pagos.")
        print("    No hay datos para generar el resumen.")
    else:
        try:
            # Validamos y sumamos asegurando que cada monto sea tratado como float
            total = sum(float(p['monto']) for p in pagos)
            
            # Conteo de métodos de pago para un reporte más detallado
            efectivo = len([p for p in pagos if p['metodo'] == 'Efectivo'])
            tarjeta = len([p for p in pagos if p['metodo'] == 'Tarjeta'])
            transferencia = len([p for p in pagos if p['metodo'] == 'Transferencia'])
            
            print(f" Total de transacciones:  {len(pagos)}")
            print("-" * 35)
            print(f" Pagos en Efectivo:       {efectivo}")
            print(f" Pagos con Tarjeta:       {tarjeta}")
            print(f" Pagos por Transferencia: {transferencia}")
            print("-" * 35)
            print(f" TOTAL RECAUDADO:         ${total:.2f}")
            
        except (ValueError, KeyError):
            print("\n[!] Error: Se detectaron datos corruptos en el archivo de pagos.")
            print("    Asegúrese de que todos los montos sean numéricos.")

    print("═"*35)
    input("\nPresione Enter para volver al menú principal...")