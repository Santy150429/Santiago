
#

import json
from almacenamiento import guardar_datos, archivo_reporte

dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves","Viernes", "Sabado", "Domingo"]

def horas_a_minutos(hora_str):
    "Convierte un str a minutos para poder comparar numericamente"

    try:
        horas, minutas = map(int, hora_str.strip().split(":"))
        return horas * 60 + minutos
    except ValueError:
        return -1

def hay_conflicto(horarios, dia, hora_inicio, hora_fin, materia_actual=None):
    "Comprueba si el rango [hora_inicio, hora_fin] choca con otra materia"
    hora_inicio_nuevo= horas_a_minutos(hora_inicio)
    hora_fin_nuevo= horas_a_minutos(hora_fin)

    if hora_inicio_nuevo == -1 or hora_fin_nuevo == -1:
        return True, "El formato de hora debe ser HH:MM (24 horas)."

    if hora_inicio_nuevo >= hora_fin_nuevo:
        return True, "La hora de inicio debe ser menor a la hora de fin."

    for evento in horarios:
        if materia_actual and evento["materia"].lower() == materia_actual.lower() and evento["dia"].lower() == dia.lower():
            continue

    if evento["dia"].lower() == dia.lower():
        hora_inicio_existente = horas_a_minutos(evento["hora_inicio"])
        hora_fin_existente = horas_a_minutos(evento["hora_fin"])

        if max(hora_inicio_nuevo, hora_inicio_existente) < min(hora_fin_nuevo, hora_fin_existente):
            return True, f"Choque de horario con '{evento['materia']}' ({evento['hora_inicio']}) - {evento['hora_fin']})."

    return False, ""
def registrar_materia(horarios, materia, dia, hora_inicio, hora_fin, ubicacion):
    "Agregar una metaria si no hay conflictos"
    conflicto, msj = hay_conflicto(horarios, dia, hora_inicio, hora_fin)
    if conflicto:
        return False, msj

    nuevo_evento = {
        "materia": materia,
        "dia": dia,
        "hora_inicio": hora_inicio,
        "hora_fin": hora_fin,
        "ubucacion": ubicacion if ubicacion else "No especificada"
    }
    horarios.append(nuevo_evento)
    guardar_datos(horarios)
    return True, "Materia registrada exitosamente."

def modificar_materia(horarios, materia_actual, nueva_materia, nuevo_dia, nueva_hora_inicio, nueva_hora_fin, nueva_ubicacion):
    "Actualiza una materia existente"
    conflicto, msj = hay_conflicto(horarios, nuevo_dia, nueva_hora_inicio, nueva_hora_fin)
    if conflicto:
        return False, msj

    nuevo_evento = {
        "materia": nueva_materia,
        "dia": nuevo_dia.capitalize(),
        "hora_inicio": nueva_hora_inicio,
        "hora_fin": nueva_hora_fin,
        "ubicacion": nueva_ubicacion if nueva_ubicacion else "sin asignacion"
    }

