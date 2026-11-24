import json


def reporte_carga_medicos():

    # Leer usuarios
    archivo = open("usuarios.json", "r", encoding="utf-8")
    usuarios = json.load(archivo)
    archivo.close()

    # Leer diagnosticos
    archivo = open("diagnosticos.json", "r", encoding="utf-8")
    diagnosticos = json.load(archivo)
    archivo.close()

    reporte = []

    # Recorrer los usuarios
    for usuario in usuarios:

        if usuario["rol"].lower() == "medico":

            id_medico = usuario["id"]
            nombre = usuario["nombre"]

            total_diagnosticos = 0
            pacientes = []
            total_sintomas = 0
            total_medicamentos = 0

            # Buscar los diagnosticos del medico
            for diagnostico in diagnosticos:

                if diagnostico["id_medico"] == id_medico:

                    total_diagnosticos += 1

                    # Contar pacientes diferentes
                    id_paciente = diagnostico["id_paciente"]

                    if id_paciente not in pacientes:
                        pacientes.append(id_paciente)

                    # Contar sintomas y medicamentos
                    total_sintomas += len(diagnostico["sintomas"])
                    total_medicamentos += len(diagnostico["medicamentos"])

            # Calcular promedios
            if total_diagnosticos > 0:
                promedio_sintomas = total_sintomas / total_diagnosticos
                promedio_medicamentos = total_medicamentos / total_diagnosticos
            else:
                promedio_sintomas = 0
                promedio_medicamentos = 0

            # Guardar informacion del medico
            medico = {
                "id_medico": id_medico,
                "nombre_completo": nombre,
                "total_diagnosticos": total_diagnosticos,
                "pacientes_distintos": len(pacientes),
                "promedio_sintomas_por_consulta": round(promedio_sintomas, 2),
                "promedio_medicamentos_por_consulta": round(promedio_medicamentos, 2)
            }

            reporte.append(medico)

    # Ordenar de mayor a menor diagnosticos
    reporte.sort(key=lambda x: x["total_diagnosticos"], reverse=True)

    # Crear resumen
    if len(reporte) > 0:

        mayor_diagnosticos = reporte[0]
        mayor_pacientes = reporte[0]
        menor_carga = reporte[0]

        for medico in reporte:

            if medico["total_diagnosticos"] > mayor_diagnosticos["total_diagnosticos"]:
                mayor_diagnosticos = medico

            if medico["pacientes_distintos"] > mayor_pacientes["pacientes_distintos"]:
                mayor_pacientes = medico

            if medico["total_diagnosticos"] < menor_carga["total_diagnosticos"]:
                menor_carga = medico

        resumen = {
            "medico_con_mayor_numero_diagnosticos": mayor_diagnosticos["nombre_completo"],
            "medico_con_mayor_numero_pacientes": mayor_pacientes["nombre_completo"],
            "medico_con_menor_carga": menor_carga["nombre_completo"]
        }

    else:
        resumen = {
            "mensaje": "No hay medicos registrados"
        }

    # Guardar el reporte
    resultado = {
        "medicos": reporte,
        "resumen": resumen
    }

    archivo = open("reporte_carga_medicos.json", "w", encoding="utf-8")
    json.dump(resultado, archivo, indent=4, ensure_ascii=False)
    archivo.close()

    print("Reporte generado correctamente")