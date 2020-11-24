print("Convertidor de dolares a colones ")
cantidad =int(input("Digite la cantidad a convertir : "))
CAMBIO=8.75
total=CAMBIO*cantidad
cabecera="la cantidad de  $ {0} dolares equivale a ¢ {1} colones.: {2}"
print (cabecera.format(cantidad	,total,CAMBIO))