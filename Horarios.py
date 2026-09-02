#generacion de horarios de clases
import json

ARCHIVO_DATOS = "horarios.json"
ARCHIVO_REPORTE = "reporte_horario.json"
DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

def hora_a_minutos(hora_str):
    """Convierte un string 'HH:MM' a minutos totales para comparar numéricamente."""
    try:
        horas, minutos = map(int, hora_str.strip().split(":"))
        return horas * 60 + minutos
    except ValueError:
        return -1

def cargar_datos():
    """Carga los eventos guardados en el archivo JSON."""
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def guardar_datos(horarios):
    """Guarda la lista de materias en el archivo JSON principal."""
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
        json.dump(horarios, f, indent=4, ensure_ascii=False)

def hay_conflicto(horarios, dia, hora_inicio, hora_fin, materia_actual=None):
    """Comprueba si el rango [hora_inicio, hora_fin] se traslapa con otra materia en el mismo día."""
    inicio_nuevo = hora_a_minutos(hora_inicio)
    fin_nuevo = hora_a_minutos(hora_fin)

    if inicio_nuevo == -1 or fin_nuevo == -1:
        return True, "El formato de hora debe ser HH:MM (24 horas)."

    if inicio_nuevo >= fin_nuevo:
        return True, "La hora de inicio debe ser menor a la hora de fin."

    for evento in horarios:
        # Si se está modificando una materia, ignora la coincidencia consigo misma
        if materia_actual and evento["materia"].lower() == materia_actual.lower() and evento["dia"].lower() == dia.lower():
            continue

        if evento["dia"].lower() == dia.lower():
            inicio_existente = hora_a_minutos(evento["hora_inicio"])
            fin_existente = hora_a_minutos(evento["hora_fin"])

            # Regla de traslape: max(inicio1, inicio2) < min(fin1, fin2)
            if max(inicio_nuevo, inicio_existente) < min(fin_nuevo, fin_existente):
                return True, f"Choque de horario con '{evento['materia']}' ({evento['hora_inicio']} - {evento['hora_fin']})."

    return False, ""

def registrar_materia(horarios, materia, dia, hora_inicio, hora_fin, ubicacion):
    """Agrega una materia si no existen conflictos."""
    conflicto, msj = hay_conflicto(horarios, dia, hora_inicio, hora_fin)
    if conflicto:
        return False, msj

    nuevo_evento = {
        "materia": materia,
        "dia": dia.capitalize(),
        "hora_inicio": hora_inicio,
        "hora_fin": hora_fin,
        "ubicacion": ubicacion if ubicacion else "Sin asignación"
    }
    horarios.append(nuevo_evento)
    guardar_datos(horarios)
    return True, f'Materia "{materia}" registrada exitosamente el {dia.capitalize()} de {hora_inicio} a {hora_fin} en {nuevo_evento["ubicacion"]}.'

def modificar_materia(horarios, materia_buscar, nuevo_dia, nueva_inicio, nueva_fin, nueva_ubicacion):
    """Actualiza una materia existente comprobando cruces de horario."""
    for evento in horarios:
        if evento["materia"].lower() == materia_buscar.lower():
            dia_evaluar = nuevo_dia if nuevo_dia else evento["dia"]
            inicio_evaluar = nueva_inicio if nueva_inicio else evento["hora_inicio"]
            fin_evaluar = nueva_fin if nueva_fin else evento["hora_fin"]

            conflicto, msj = hay_conflicto(horarios, dia_evaluar, inicio_evaluar, fin_evaluar, materia_actual=materia_buscar)
            if conflicto:
                return False, msj

            evento["dia"] = dia_evaluar.capitalize()
            evento["hora_inicio"] = inicio_evaluar
            evento["hora_fin"] = fin_evaluar
            if nueva_ubicacion:
                evento["ubicacion"] = nueva_ubicacion

            guardar_datos(horarios)
            return True, f'Materia "{evento["materia"]}" modificada exitosamente a {evento["dia"]} de {evento["hora_inicio"]} a {evento["hora_fin"]} en {evento["ubicacion"]}.'

    return False, f'No se encontró la materia "{materia_buscar}".'

def eliminar_materia(horarios, materia, dia):
    """Elimina la materia según nombre y día especificado."""
    for i, evento in enumerate(horarios):
        if evento["materia"].lower() == materia.lower() and evento["dia"].lower() == dia.lower():
            del horarios[i]
            guardar_datos(horarios)
            return True, f'La materia "{materia}" ha sido eliminada del horario del día {dia.capitalize()}.'
    return False, f'No se encontró la materia "{materia}" el día {dia.capitalize()}.'

def generar_reporte(horarios):
    """Estructura el reporte por días y lo guarda en 'reporte_horario.json'."""
    reporte = []
    for dia in DIAS_SEMANA:
        eventos_dia = [
            {
                "materia": e["materia"],
                "hora_inicio": e["hora_inicio"],
                "hora_fin": e["hora_fin"],
                "ubicacion": e["ubicacion"]
            }
            for e in horarios if e["dia"].capitalize() == dia
        ]
        if eventos_dia:
            reporte.append({
                "dia": dia,
                "eventos": eventos_dia
            })

    with open(ARCHIVO_REPORTE, "w", encoding="utf-8") as f:
        json.dump(reporte, f, indent=4, ensure_ascii=False)

    return reporte
        