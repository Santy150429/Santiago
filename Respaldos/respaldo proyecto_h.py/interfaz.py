
#Muestra toda la informacion de los horarios

def limpiar_texto(texto):
    "Convierte a minúsculas, elimina espacios extras y remueve tildes"
    texto = texto.lower().strip()
    reemplazos = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
    for origen, destino in reemplazos:
        texto = texto.replace(origen, destino)
    return texto

def ver_horario_semanal(horarios, estudiante):
    "Muestra el horario semanal de un estudiante"

    materias_estudiante = []
    for evento in horarios:
        if limpiar_texto(evento.get("estudiante", "")) == limpiar_texto(estudiante):
            materias_estudiante.append(evento)

    if not materias_estudiante:
        print(f"\nNo hay materias registradas para {estudiante}")
        return

    print("\n" + "=" * 95)
    print(f"HORARIO DE: {estudiante.upper()}")
    print("=" * 95)
    print(f"{'Hora':<15} | {'Lunes':<12} | {'Martes':<12} | {'Miercoles':<12} | {'Jueves':<12} | {'Viernes':<12}")
    print("=" * 95)

    franjas = [
        ("08:00-10:00", "08:00"),
        ("10:00-12:00", "10:00"),
        ("12:00-13:00", "12:00"),
        ("13:00-15:00", "13:00"),
        ("15:00-17:00", "15:00") 
    ]

    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

    for franja, hora_inicio in franjas:
        fila = f"{franja:<15} | "

        for dia in dias:
            actividad = "Almuerzo" if franja == "12:00-13:00" else "Libre"

            for evento in materias_estudiante:
                h_ev = evento["hora_inicio"].zfill(5)
                # Normaliza ambos textos antes de comparar
                if limpiar_texto(dia) in limpiar_texto(evento["dia"]) and h_ev == hora_inicio: 
                    actividad = evento["materia"]
                    break 
            
            fila += f"{actividad:<12} | "
        
        print(fila)
        
    print("=" * 95)