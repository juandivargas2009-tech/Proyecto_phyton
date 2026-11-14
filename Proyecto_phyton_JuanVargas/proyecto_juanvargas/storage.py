import json
import os

ARCHIVO_DATOS = "data.json"

def inicializar_base_datos():
    """Crea el archivo JSON general con el administrador y el doctor por defecto si no existe."""
    if not os.path.exists(ARCHIVO_DATOS):
        datos_iniciales = {
            "usuarios": [
                {
                    "identificacion": "0000",
                    "nombres": "Admin",
                    "apellidos": "Administrador",
                    "telefono": "555 000111",
                    "email": "admin@acmeclinic.com",
                    "direccion": "Cl 185 # 26 – 85",
                    "password": "admin",
                    "rol": "Administrador"
                },
                {
                    "identificacion": "1111",
                    "nombres": "Carlos",
                    "apellidos": "Pérez",
                    "telefono": "555 222333",
                    "email": "doctor@acmeclinic.com",
                    "direccion": "Cl 100 # 15-20",
                    "password": "doctor123",
                    "rol": "Médico"
                }
            ],
            "pacientes": [],
            "diagnosticos": []
        }
        guardar_datos(datos_iniciales)

def cargar_datos():
    """Lee y carga la información del archivo JSON general."""
    inicializar_base_datos()
    with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def guardar_datos(datos):
    """Guarda y actualiza la información en el archivo JSON general."""
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)