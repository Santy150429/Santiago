
#Muestra toda la informacion de los horarios

def ver_horario_semanal(horarios):
    "Muestra el horario semanal"
    if not horarios:
        print("\nNo hay materias registradas en el horario")
        return

    print("\n" + "="*85)
    print(f"{"hora", :<15} | {"lunes", :<12} | {"martes", :<12} | {"miercoles", :<12} | {"jueves", :<12} | {"viernes", :12}")
    print("="*85)

    franjas = ["8:00-10:00", "10:00-12:00", "12:00-13:00", "13:00-15:00", "15:00-17:00"]
    dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

    for franja in franjas:
        if franja == "12:00-13:00":
            fila = f"{franja:<15} | "
            for _ in dias_semana:
                fila += f"{"Almuerzo", :<12} | "
            print(fila)
            continue 
        hora_inicio = franja[:5]
        fila = f"{franja:<15} | "
        for dia in dias_semana:
            actividad = "libre"
            for evento in horarios:
                if evento["dia"].lower() == dia.lower() and evento["hora_inicio"] == hora_inicio:
                    actividad = evento["materia"]
                break
            fila += f"{actividad:<12} | "
            print(fila)      