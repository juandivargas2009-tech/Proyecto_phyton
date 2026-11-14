from datetime import datetime
import json
from storage import cargar_datos, guardar_datos

def diagnosticar_paciente(usuario_actual):
    """
    Realiza el diagnóstico y genera la prescripción médica.
    RESTRICCIÓN: Solo el personal con rol 'Médico' puede ejecutar esta función. 
    El Administrador tiene prohibido diagnosticar.
    """
    # Validamos estrictamente que el usuario sea Médico
    if usuario_actual["rol"] != "Médico":
        print("\n[ERROR] Acceso denegado. El administrador no puede realizar diagnósticos; esta función es exclusiva del médico.")
        return

    print("\n--- DIAGNOSTICAR PACIENTE ---")
    id_paciente = input("Ingrese el número de identificación del paciente: ").strip()
    
    datos = cargar_datos()
    
    paciente_encontrado = None
    for p in datos["pacientes"]:
        if p["identificacion"] == id_paciente:
            paciente_encontrado = p
            break
            
    if not paciente_encontrado:
        print("\n[ERROR] El paciente debe estar registrado previamente en el sistema.")
        return

    print(f"\nPaciente encontrado: {paciente_encontrado['nombres']} {paciente_encontrado['apellidos']}")
    
    sintomas = input("Registre los síntomas y aflicciones del paciente: ").strip()
    diagnostico_texto = input("Describa la patología o enfermedad del paciente: ").strip()
    
    print("\n--- Prescripción Médica ---")
    medicamento = input("Nombre del medicamento: ").strip()
    cantidad = input("Cantidad: ").strip()
    dosis = input("Dosis (cuánto tomar diariamente): ").strip()
    tiempo_aplicacion = input("Tiempo de aplicación (días de duración): ").strip()

    fecha_legible = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fecha_archivo = datetime.now().strftime("%Y%m%d_%H%M%S")

    prescripcion = {
        "medicamento": medicamento,
        "cantidad": cantidad,
        "dosis": dosis,
        "tiempo_aplicacion": tiempo_aplicacion
    }

    nuevo_diagnostico = {
        "fecha": fecha_legible,
        "paciente_id": paciente_encontrado["identificacion"],
        "paciente_nombre": f"{paciente_encontrado['nombres']} {paciente_encontrado['apellidos']}",
        "medico": f"{usuario_actual['nombres']} {usuario_actual['apellidos']}",
        "sintomas": sintomas,
        "diagnostico": diagnostico_texto,
        "prescripcion": prescripcion
    }

    # 1. Guardar en la base de datos general (data.json)
    datos["diagnosticos"].append(nuevo_diagnostico)
    guardar_datos(datos)

    # 2. Generar el archivo JSON independiente de la prescripción
    nombre_archivo_json = f"prescripcion_paciente_{id_paciente}_{fecha_archivo}.json"
    with open(nombre_archivo_json, "w", encoding="utf-8") as archivo_json:
        json.dump(nuevo_diagnostico, archivo_json, indent=4, ensure_ascii=False)

    print(f"\n[ÉXITO] Diagnóstico registrado y archivo JSON de prescripción generado: '{nombre_archivo_json}'")