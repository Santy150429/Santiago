#Funcion open()

#abrir un arcivo llamado archivo_plano.txt

#pro defecto de lectura
file=open("archivo.txt")

#read()para leer los valores en la variavle
print(file.read())

#cerrar el archivo despues de usar
file.close()

#Escritura de archivos, w crea sino existe un archivo previo
file=open("nuevo_archivo_plano.txt","w")
file.write("confirmando el paso de infotmacion")
file.close()

#Lectura de archivos con with
with open("nuevo_archivo_plano.txt","r") as f:
    print(f.read())

#añadir informacion a nuevo_archivo_palno.txt


#Lectura y escritura
with open("nuevo_archivo_plano.txt","r+") as archivo:
    contenido=archivo.read()
    print(contenido)
    archivo.write("\n Otra nanada mas")



    