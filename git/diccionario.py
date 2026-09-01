primer_diccionario={"nombre":"mazda","color":"blanco","año":2020,"habilitado":True}
print(primer_diccionario["nombre"])
print(primer_diccionario["color"])  

Usuario=dict([("nombre","sara"),("edad",27),("documento",123)])
print(Usuario)

usuario = dict(
Nombre="sara",
Edad=27,
Documento=1003882
)

#forma de traer valores de los directorios
print(Usuario["Documento"])
print(Usuario.get("Nombre"))

#Modificar valor de la fireccion
Usuario["Documento"]=10382
print(Usuario.get("Documento"))

#Puedo agregar llaves, o modificarlas
Usuario["sexo"]="Femenino"
print(Usuario)

#Recorrer un diccionario
for clave in Usuario:
    print(clave)

#Recorrer un diccionario con valores
for clave in Usuario:
    print(clave,Usuario[clave])

#items() permite obtener ambos elementos en cada iteraccion
for llave,valor in Usuario.items():
    print(llave,valor)

#Limpiar datos en un diccionario
#Usuario.clear()
#print(Usuario)

#keys me trae las llaves a keys de un diccionario
print(list(Usuario.keys()))

#para trae los valores con values()
print(list(Usuario.values()))

#pop, Elimina y devuelve el varor

Usuario.pop("sexo")
print(Usuario)

#update, combina o actualiza un diccionario con los datos de otro diccionario
diccionario1={"a":100,"b":200,"c":True}
diccionario1_verdadero={"a":100,"b":200,"c":True}

diccionario1.update(diccionario1_verdadero)
print(diccionario1)

Productos = {
    "menta": {"casto":40, "precio":300, "cantidadDisponible": 10},
    "Chocorramo": {"casto":700, "precio":1000, "cantidadDisponible": 12}, 
} 

print("productos"["menta"]["costo"]["productos"]["menta"]["costo"])