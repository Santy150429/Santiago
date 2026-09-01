#Ejercicio sistema de tarifas
tarifas = {
    "moto": 1500,
    "carro": 3000,
    "bus": 5000
}

vehiculo = input("Ingrese el tipo de vehículo (moto, carro o bus): ").lower()
horas = int(input("Ingrese la cantidad de horas: "))

if vehiculo in tarifas:
    total = tarifas[vehiculo] * horas
    print("El valor total a pagar es: $", total)
else:
    print("No se reconoce ese tipo de vehículo.")