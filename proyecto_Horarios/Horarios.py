#generacion de horarios de clases

import json
import os

def cargar_datos():
    if not os.path.exists("horarios.json"):
        return []
    with open("horarios.json", "r") as archivos:
        return json.load(archivos)

horarios = cargar_datos()

def guardar_datos():
    with open("horarios.json", "w") as archivos:
        json.dump(horarios, archivos, indent=4)

while True:
    print("\n==========================================")
    print("Generador de horarios de clases")
    print("\n==========================================")
    print("1. Agregar clase o actividad")
    print("2. Ver horarios semanal")
    print("3. Modificar clase o actividad")
    print("4. Eliminar clase o actividad")
    print("5. Generar reporte de horarios")
    print("6. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        