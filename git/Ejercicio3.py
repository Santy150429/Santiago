from datetime import datetime


def registrar_ingreso():
    nombre = input("Ingrese el nombre del estudiante: ")
    codigo = input("Ingrese el código estudiantil: ")

    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("bitacora.txt", "a") as archivo:
        archivo.write(f"{nombre},{codigo},{fecha_hora}\n")

    print("Ingreso registrado correctamente.")


def consultar_bitacora():
    try:
        with open("bitacora.txt", "r") as archivo:
            contenido = archivo.read()

        if contenido:
            print("\n--- BITÁCORA COMPLETA ---")
            print(contenido)
        else:
            print("La bitácora está vacía.")

    except FileNotFoundError:
        print("Todavía no existe la bitácora.")


def contar_estudiantes():
    estudiantes = set()

    try:
        with open("bitacora.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")

                if len(datos) >= 2:
                    codigo = datos[1]
                    estudiantes.add(codigo)

        print(f"\nEstudiantes distintos que ingresaron: {len(estudiantes)}")

    except FileNotFoundError:
        print("Todavía no existe la bitácora.")


while True:
    print("\n===== LABORATORIO =====")
    print("1. Registrar ingreso")
    print("2. Consultar bitácora")
    print("3. Contar estudiantes distintos")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_ingreso()

    elif opcion == "2":
        consultar_bitacora()

    elif opcion == "3":
        contar_estudiantes()

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")