from auth import iniciar_sesion
from pacientes import registrar_paciente
from diagnosticos import diagnosticar_paciente
from historial import consultar_historia_clinica

def main():
    """Función principal que coordina el flujo de la aplicación de la Clínica ACME."""
    while True:
        print("\n==================================================")
        print("      SISTEMA DE GESTIÓN - CLÍNICA ACME           ")
        print("==================================================")
        
        # Login obligatorio al iniciar el programa
        usuario_actual = iniciar_sesion()
        
        if usuario_actual:
            while True:
                print(f"\n--- MENÚ PRINCIPAL (Usuario: {usuario_actual['nombres']} | Rol: {usuario_actual['rol']}) ---")
                print("1. Registrar nuevo paciente")
                print("2. Diagnosticar paciente y generar prescripción JSON")
                print("3. Consultar historia clínica de un paciente")
                print("4. Cerrar sesión (Volver al Login)")
                
                opcion = input("Seleccione una opción (1-4): ").strip()
                
                if opcion == "1":
                    registrar_paciente()
                elif opcion == "2":
                    diagnosticar_paciente(usuario_actual)
                elif opcion == "3":
                    consultar_historia_clinica()
                elif opcion == "4":
                    print("\n[INFO] Sesión cerrada correctamente. Volviendo al Login...")
                    break
                else:
                    print("\n[ERROR] Opción inválida. Ingrese un número del 1 al 4.")

if __name__ == "__main__":
    main()