
#

import json
from almacenamiento import guardar_datos, guardar_reporte

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

def horas_a_minutos(hora_str):
    try:
        horas, minutos = map(int, hora_str.strip().split(":"))
        return horas * 60 + minutos
    except ValueError:
        return -1

def hay_conflicto(horarios, estudiante, dia, hora_inicio, hora_fin, materia_actual=None):
    hora_inicio_nuevo = horas_a_minutos(hora_inicio)
    hora_fin_nuevo = horas_a_minutos(hora_fin)

    if hora_inicio_nuevo == -1 or hora_fin_nuevo == -1:
        return True, "El formato de hora debe ser HH:MM (24 horas)."

    if hora_inicio_nuevo >= hora_fin_nuevo:
        return True, "La hora de inicio debe ser menor a la hora de fin."

    for evento in horarios:
        if evento.get("estudiante", "").lower() == estudiante.lower():
            if materia_actual and evento["materia"].lower() == materia_actual.lower() and evento["dia"].lower() == dia.lower():
                continue

            if evento["dia"].lower() == dia.lower():
                hora_inicio_existente = horas_a_minutos(evento["hora_inicio"])
                hora_fin_existente = horas_a_minutos(evento["hora_fin"])

                if max(hora_inicio_nuevo, hora_inicio_existente) < min(hora_fin_nuevo, hora_fin_existente):
                    return True, f"Choque de horario con '{evento['materia']}' ({evento['hora_inicio']} - {evento['hora_fin']})."

    return False, ""

def registrar_materia(horarios, estudiante, materia, dia, hora_inicio, hora_fin, ubicacion):
    conflicto, msj = hay_conflicto(horarios, estudiante, dia, hora_inicio, hora_fin)
    if conflicto:
        return False, msj

    nuevo_evento = {
        "estudiante": estudiante,
        "materia": materia,
        "dia": dia.capitalize(),
        "hora_inicio": hora_inicio,
        "hora_fin": hora_fin,
        "ubicacion": ubicacion if ubicacion else "No especificada"
    }
    horarios.append(nuevo_evento)
    guardar_datos(horarios)
    return True, f"Materia registrada exitosamente para {estudiante}."

def modificar_materia(horarios, estudiante, materia_actual, nueva_materia, nuevo_dia, nueva_hora_inicio, nueva_hora_fin, nueva_ubicacion):
    conflicto, msj = hay_conflicto(horarios, estudiante, nuevo_dia, nueva_hora_inicio, nueva_hora_fin, materia_actual)
    if conflicto:
        return False, msj

    encontrado = False
    for evento in horarios:
        if evento.get("estudiante", "").lower() == estudiante.lower() and evento["materia"].lower() == materia_actual.lower():
            evento["materia"] = nueva_materia
            evento["dia"] = nuevo_dia.capitalize()
            evento["hora_inicio"] = nueva_hora_inicio
            evento["hora_fin"] = nueva_hora_fin
            evento["ubicacion"] = nueva_ubicacion if nueva_ubicacion else "Sin asignacion"
            encontrado = True
            break

    if not encontrado:
        return False, f"No se encontro la materia '{materia_actual}' para {estudiante}."

    guardar_datos(horarios)
    return True, "Materia actualizada exitosamente."

def eliminar_materia(horarios, estudiante, materia):
    nuevos_horarios = []
    encontrado = False

    for evento in horarios:
        if evento.get("estudiante", "").lower() == estudiante.lower() and evento["materia"].lower() == materia.lower():
            encontrado = True
        else:
            nuevos_horarios.append(evento)

    if not encontrado:
        return False, f"No se encontro la materia '{materia}' para {estudiante}."

    horarios.clear()
    horarios.extend(nuevos_horarios)
    guardar_datos(horarios)
    return True, f"Materia '{materia}' de {estudiante} eliminada correctamente."

def generar_reporte(horarios):
    total = len(horarios)
    reporte = {
        "total_materias_registradas": total,
        "detalle": horarios
    }
    guardar_reporte(reporte)
    return True, "Reporte generado en 'reporte_horario.json'."