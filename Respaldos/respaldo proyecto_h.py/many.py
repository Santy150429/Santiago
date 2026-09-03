
from almacenamiento import cargar_datos
from interfaz import ver_horario_semanal
from operaciones import registrar_materia, modificar_materia, eliminar_materia, generar_reporte

def menu():
    horarios = cargar_datos()

    while True:
        print("\n" + "=" * 35)
        print("     SISTEMA DE HORARIOS")
        print("=" * 35)
        print("1. Ver horario de un estudiante")
        print("2. Registrar nueva materia")
        print("3. Modificar materia")
        print("4. Eliminar materia")
        print("5. Generar reporte JSON")
        print("6. Salir")

        opcion = input("\nElige una opcion (1-6): ").strip()

        if opcion == "1":
            estudiante = input("Nombre del estudiante: ").strip()
            ver_horario_semanal(horarios, estudiante)

        elif opcion == "2":
            print("\n--- Registrar Materia ---")
            estudiante = input("Nombre del estudiante: ").strip()
            materia = input("Nombre de la materia: ").strip()
            dia = input("Dia de la semana (ej. Lunes): ").strip()
            hora_inicio = input("Hora inicio (HH:MM): ").strip()
            hora_fin = input("Hora fin (HH:MM): ").strip()
            ubicacion = input("Ubicacion o salon: ").strip()

            exito, msj = registrar_materia(horarios, estudiante, materia, dia, hora_inicio, hora_fin, ubicacion)
            print("\n" + msj)

        elif opcion == "3":
            print("\n--- Modificar Materia ---")
            estudiante = input("Nombre del estudiante: ").strip()
            materia_actual = input("Materia que quieres cambiar: ").strip()
            nueva_materia = input("Nuevo nombre de materia: ").strip()
            nuevo_dia = input("Nuevo dia: ").strip()
            nueva_hora_inicio = input("Nueva hora inicio (HH:MM): ").strip()
            nueva_hora_fin = input("Nueva hora fin (HH:MM): ").strip()
            nueva_ubicacion = input("Nueva ubicacion: ").strip()

            exito, msj = modificar_materia(
                horarios, estudiante, materia_actual, nueva_materia, 
                nuevo_dia, nueva_hora_inicio, nueva_hora_fin, nueva_ubicacion
            )
            print("\n" + msj)

        elif opcion == "4":
            print("\n--- Eliminar Materia ---")
            estudiante = input("Nombre del estudiante: ").strip()
            materia = input("Materia a eliminar: ").strip()

            exito, msj = eliminar_materia(horarios, estudiante, materia)
            print("\n" + msj)

        elif opcion == "5":
            exito, msj = generar_reporte(horarios)
            print("\n" + msj)

        elif opcion == "6":
            print("\nChao, saliendo del programa...")
            break

        else:
            print("\nOpcion invalida, intenta de nuevo.")

if __name__ == "__main__":
    menu()