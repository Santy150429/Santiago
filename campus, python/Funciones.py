
#funciones
def Saludar(nombre,lenguaje):
    print("Hola ", nombre, "buenvenidos al imalaya:", lenguaje)

#invocar
Saludar("santiago","parte india")

#funcion con numero de argumentos indefinidos
def compras(*productos):
    print(productos)


compras("peruano", "chclitos", "huevo", "queso asul sin z") 

#funcion de promedio de notas
def calcular_promedio_notas(nota1=0,nota2=0,nota3=0):
    promedio=(nota1+nota2+nota3)/3
    return promedio

print(calcular_promedio_notas(70,80,90))
print(calcular_promedio_notas())
print(calcular_promedio_notas(90))

#sub-funciones: finciones dentro de funciones
def funcion_externa(x):
    def funcion_interna(y):
        return x+y
    return funcion_interna

subfuncion1=funcion_externa(10)
print(subfuncion1(5))

#refactorisar, cajero automatico, cuantos billetes de cada denominacion debe de entregar un cajero 
#dado un monto que el usuario pida
 
def retiro_denominacion_billetes():
    cantidad=int(input("por favor digita la cantidad a retirar: "))
    cincuenta_mil=0
    veinte_mil=0
    while (cantidad>=50000):
        cincuenta_mil+=1
        cantidad-=50000
    while (cantidad>=20000):
        veinte_mil+=1
        cantidad-=20000 
    print("la cantidad de billetes de 50.000 son:",cincuenta_mil)    
    print("la cantidad de billetes de 20.000 son:",veinte_mil) 

#185.000
retiro_denominacion_billetes()

#alcance variable

persona="elon musk"

def campuslands():
    global persona
    persona="johlver"
    return persona

campuslands()
print("la persona es: ",persona)




