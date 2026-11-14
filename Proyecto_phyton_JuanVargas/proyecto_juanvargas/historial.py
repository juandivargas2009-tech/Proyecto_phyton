from storage import cargar_datos

def consultar_historia_clinica():
    """Muestra la historia clínica de un paciente (encabezado y cuerpo de consultas)."""
    print("\n--- HISTORIA CLÍNICA ---")
    id_paciente = input("Ingrese el número de identificación del paciente: ").strip()
    
    datos = cargar_datos()
    
    paciente = None
    for p in datos["pacientes"]:
        if p["identificacion"] == id_paciente:
            paciente = p
            break
            
    if not paciente:
        print("\n[ERROR] No se encontró ningún paciente con ese número de identificación.")
        return

    print("\n" + "="*50)
    print("          ENCABEZADO - DATOS DEL PACIENTE          ")
    print("="*50)
    print(f"Identificación : {paciente['identificacion']}")
    print(f"Nombres        : {paciente['nombres']} {paciente['apellidos']}")
    print(f"Teléfono       : {paciente['telefono']}")
    print(f"E-mail         : {paciente['email']}")
    print(f"Dirección      : {paciente['direccion']}")
    print(f"Género         : {paciente['genero']}")
    print(f"Estado Civil   : {paciente['estado_civil']}")
    print("="*50)

    consultas_paciente = []
    for d in datos["diagnosticos"]:
        if d["paciente_id"] == id_paciente:
            consultas_paciente.append(d)

    if not consultas_paciente:
        print("\n[INFO] El paciente no registra consultas previas en el sistema.")
    else:
        print(f"\nCUERPO DEL HISTORIAL ({len(consultas_paciente)} consulta(s)):")
        for i, c in enumerate(consultas_paciente, 1):
            print(f"\n--- Consulta #{i} ---")
            print(f"Fecha              : {c['fecha']}")
            print(f"Médico que atendió : {c['medico']}")
            print(f"Síntomas           : {c['sintomas']}")
            print(f"Diagnóstico        : {c['diagnostico']}")
            print("Prescripción Médica:")
            p = c["prescripcion"]
            print(f"  * Medicamento    : {p['medicamento']}")
            print(f"  * Cantidad       : {p['cantidad']}")
            print(f"  * Dosis          : {p['dosis']}")
            print(f"  * Duración       : {p['tiempo_aplicacion']} días")
    print("="*50)