print("Hola mundo")

booleano_vedadero=True
booleano_falso=False

print(booleano_vedadero)
print(booleano_falso)

dato_numerico_entero= 16
dato_numerico_decimal= 16.5

#Cadena de caracteres o string.
cadena_caracteres="campus"

#forma que se devuelca el tipo de dato
print(type(cadena_caracteres))

#cambercion de tipos de datos
print(int(dato_numerico_decimal))

print(float(dato_numerico_entero))

numero_cadena_caracter="26"
print(int(numero_cadena_caracter))

numero_a=5
numero_b=10
#print(numero_a)
#print(numero_b)

print(f"Los numeros impresos con {numero_a} y {numero_b}")

#Operacion de cadena

cadena="Esto es una cadena"

#Imprimir primer caracter
print(cadena[0:])

#Metodos avanzados de cadenas
#find(), replace(), upper(), lower(), capitalize(), title(), split(), join()

#find() busca una palabra o subcadena y me devuelve la posicion dende empieza
indice=cadena.find("cadena")

#replace(), remplaza una palabra por otra sin cambiar la cadena original
nueva_cadena=cadena.replace("cadena","python")
print(nueva_cadena)

otra_cadena= "Hola mundo"

#upper() los pone en mayusculas
print(otra_cadena.upper())

#lower() los pone en minuscula
print(otra_cadena.lower())

#capitalize() el primer indice de la cadena lo pone en mayuscula
print(otra_cadena.capitalize())

#title si me hace la primera en mayuscula de cada palabra
print(otra_cadena.title())

la_cadena="hola, como, estas"

#split() separa las cadenas y crea una lista, usar comas como referencia de corte
subcadena=la_cadena.split(",")
print(subcadena)

#join( une los elemantos de una lista en una sola cadena,usando un elemento separador
new_cadena="-".join(subcadena)
print(new_cadena)

#Operador
numero1=0

#metodo, largo numero1=numero1+1
#metodo, corto numero1+=1

numero1+=1
print(numero1)

numero2=1

numero2*=3
print(numero2)

#operador relacionales
variable1=5
variable2=10
variable3=5
variable4=10
variable5=5
variable6=10

print(variable1==variable2) #si es igual
print(variable3!=variable4) #si es diferente
print(variable5<=variable6) #si es menor que

#OPERADORES logicos
#and, or y not

#and= las dos repuestas o las 2 opciones deben ser verdaderas para que la respuesta sea verdadera
hay_luz=True
hay_internet=True

print("se puede hacer la clase")
print(hay_luz==True and hay_internet==True)

#almenos una de las dos respuestas debe ser verdadero
compañia_padre=True
compañia_madre=True

print("puede ir el niño al parque")
print(compañia_madre or compañia_padre)

#not inbierte el resutado logico

que_tienes=False

print(not(que_tienes))

#condicionales en python
#si la condicion se cumple se ejecuta unas linesas de codigo
edad=18
if edad<14:
    print("Es un niñ@")
elif edad<18:
    print("Es un adolecente")
elif edad<65:
    print("Un adulto")
else:
    print("Un anciano")

#new skill
palabra="programacion"

letra_buscada="z"
indice=0

while (True):
    if (indice>=len(palabra)):
        print("La letrano se encontro")
        break #si llega a esta parte, se sale del bucle
    if(palabra[indice]==letra_buscada):
        print("La letra esta en la posicion: ", indice)
        break
    indice+=1

#Estructura repetitiva for
for numero in range(30,42,2):
    print(numero)

#Contar cuantas veces aparece la letra a en una cadena
cadena=input("Ingrese una cadena de texto para saber si tiene letras a")
cuenta=0

for caracter in cadena:
    if caracter == "a":

        cuenta+=1

        print("La cantidad de a encontados son: {cuenta}")

