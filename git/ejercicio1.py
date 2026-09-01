#ejercicio 1,lista de compras
compras=["arroz","queso","pan","huevo"]

#agregar un producto
producto=input("Ingrese un producto para agregarlo:")

if producto in compras:
    print("El ya esta en la lista:")
else:
    compras.append(producto)
    print("Producto agregado correctamente.")

#ingresar un producto urgente
urgente=input("Ingrese un producto urgente:")

if urgente in compras:
    print("EL producto ya esta en la lista")
else:
    compras.insert(0,urgente)
    print("Producto urgente que ya no necesita:")

#Eliminar un producto
eliminar=input("Ingrese el producto que ya no necesita:")

if eliminar in compras:
    print("Ese producto ya no esta en la lista:")

if eliminar in compras:
    compras.remove(eliminar)
    print("Producto eliminado correctamente.")
else:
    print("Ese producto no esta en la lista.")

#Ordenar lista
compras.sort()

#Mostrar lista
print("Lista de compras ordenada:")
print(compras)
