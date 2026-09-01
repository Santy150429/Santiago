from collections.abc import Iterable

print(type("40"))

#que me imprima verdadero si es un objeto iterable
def es_iterable(obj): 
    print( issubclass(type(obj),Iterable) )
    
numero_etero=3
cadena="cadena"
booleano=Truenumero_decimal=40.5
diccionario={"nombre":"juan","apellido":"paz"}

es_iterable(diccionario)