#Manejo de excepciones
try:
    numero1=int(input("introduce el primer numero:"))
    numero2=int(input("introduce el segundo numero:"))
    division=numero1/numero2

    #intertar convertir tecto no numerico
except ValueError:
    print("debes de usar solo numeros")
except ZeroDivisionError:
    print("nu puedes divider entre cero")
else:
    print(division)
finally:
    print("esto se ejecuta haya o no haya error")