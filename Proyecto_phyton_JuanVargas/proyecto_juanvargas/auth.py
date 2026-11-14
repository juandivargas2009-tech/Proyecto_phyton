from storage import cargar_datos

def iniciar_sesion():
    """Interfaz de Login: valida el e-mail corporativo y la contraseña asignada."""
    print("\n" + "="*50)
    print("        CLÍNICA ACME - ACCESO AL SISTEMA")
    print("="*50)
    print("Credenciales de prueba disponibles:")
    print(" - Admin   -> admin@acmeclinic.com / admin")
    print(" - Médico  -> doctor@acmeclinic.com / doctor123")
    print("-"*50)
    
    email_ingresado = input("E-mail corporativo (Usuario): ").strip()
    password_ingresado = input("Contraseña: ").strip()
    
    datos = cargar_datos()
    
    for usuario in datos["usuarios"]:
        if usuario["email"] == email_ingresado and usuario["password"] == password_ingresado:
            print(f"\n[ÉXITO] ¡Bienvenido/a, {usuario['nombres']} {usuario['apellidos']}!")
            return usuario
            
    print("\n[ERROR] E-mail o contraseña incorrectos. Acceso denegado.")
    return None