from file_manager import FileManagerPago

def ejecutar_reportes_spa():
    fm_p = FileManagerPago()
    print("\n" + "="*30)
    print("      RESUMEN FINANCIERO")
    print("="*30)
    
    pagos = fm_p.get_all()
    total = sum(float(p['monto']) for p in pagos)
    
    print(f"Pagos realizados: {len(pagos)}")
    print(f"Total Recaudado:  ${total:.2f}")
    print("="*30)
    input("\nPresione Enter para volver...")