from storage import cargar_datos, guardar_datos

def registrar_paciente():
    """Registra un nuevo paciente en el sistema."""
    print("\n--- REGISTRO DE PACIENTE ---")
    id_paciente = input("Número de identificación: ").strip()
    
    datos = cargar_datos()
    
    for p in datos["pacientes"]:
        if p["identificacion"] == id_paciente:
            print("\n[ERROR] El paciente ya se encuentra registrado.")
            return

    nombres = input("Nombres: ").strip()
    apellidos = input("Apellidos: ").strip()
    telefono = input("Número de teléfono: ").strip()
    email = input("E-mail: ").strip()
    direccion = input("Dirección: ").strip()
    genero = input("Género: ").strip()
    estado_civil = input("Estado civil: ").strip()

    nuevo_paciente = {
        "identificacion": id_paciente,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "genero": genero,
        "estado_civil": estado_civil
    }

    datos["pacientes"].append(nuevo_paciente)
    guardar_datos(datos)
    print("\n[ÉXITO] Paciente registrado correctamente.")