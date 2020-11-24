lista=[]
for k in range(3):
	lista.append(input("introduce un valor en la lista:"))
print ("Los elementos de la lista son :"+ str(lista))

# modifica el valor de la lista
valor=int(input("introduce el valor a modificar de la lista pon el indice : "))
nuevo=input("Ingrese el numero: ")
lista[valor]=nuevo
print ("Los elementos de la lista son :"+ str(lista))


# Agrega un valor en la lista
valor=int(input("introduce el valor a agregar de la lista pon el indice : "))
nuevo=input("Ingrese el numero: ")
lista.insert(valor,nuevo)
print ("Los elementos de la lista son :"+ str(lista))


# Elimina un valor en la lista

nuevo=input("Ingrese el numero a eliminar: ")
lista.remove(nuevo)
print ("Los elementos de la lista son :"+ str(lista))

# busca un valor en la lista

nuevo=input("Ingrese el numero a buscar en la lista: ")
resultado=(nuevo in lista)
if (resultado):
	print("Existe elemento y su indice es: " + str(lista.index(nuevo)))
else:
	print("No existe")