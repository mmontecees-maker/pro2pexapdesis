import os
import sys

# Forzamos a Python a reconocer la carpeta actual para evitar errores de importación
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importaciones de los módulos del SPA
from menus.menu_principal import mostrar_menu_principal
from actions.acciones_clientes import ejecutar_menu_clientes
from actions.acciones_empleados import ejecutar_menu_empleados
from actions.acciones_servicios import ejecutar_menu_servicios
from actions.acciones_citas import ejecutar_proceso_cita  # Incluye detalle_cita
from actions.acciones_pagos import ejecutar_menu_pagos
from actions.acciones_reportes import ejecutar_reportes_spa

def main():
    while True:
        # Limpiar pantalla según el sistema operativo
        os.system("cls" if os.name == "nt" else "clear")
        
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Gestión de Clientes (Datos personales, historial)
            ejecutar_menu_clientes()
            
        elif opcion == "2":
            # Gestión de Empleados (Terapeutas, especialistas)
            ejecutar_menu_empleados()
            
        elif opcion == "3":
            # Gestión de Servicios (Masajes, faciales, depilación, etc.)
            ejecutar_menu_servicios()
            
        elif opcion == "4":
            # Gestión de Citas y Detalle_Cita (Agendar, asignar cabina/empleado)
            ejecutar_proceso_cita()
            
        elif opcion == "5":
            # Gestión de Pagos (Facturación de servicios realizados)
            ejecutar_menu_pagos()
            
        elif opcion == "6":
            # Reportes (Citas del día, ingresos por servicio)
            ejecutar_reportes_spa()
            
        elif opcion == "7":
            print("\nSaliendo del SISTEMA SPA. ¡Que tenga un día relajante!")
            break
            
        else:
            print("\n[!] Opción inválida.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()