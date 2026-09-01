#convertir una estructura json a estructura datos python
import json
file=open("object.json")
users=json.load(file)
#me trae el archivo como una lista
#print(users[0])

for user in users:
    print("Nombre: ", user["name"], "edad: ", user["age"])

file.close()

#comvertir una estructura de datos de python a formato json
#dumps(), practicamente me comvierte una lista a una lista de diccionarios a json
diccionario=[
    "123",{"nombre":"juan",
           "fecha_nacimiento":"2000-12-12",
           "altura":1.82,
           "hijos":1,
           "trabajador":True  
          }                
]

diccionario_json=json.dumps(diccionario)
file2=open("dicionario_json.json","w")
file2.write(diccionario_json)
file2.close()