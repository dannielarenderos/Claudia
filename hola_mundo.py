print("datos de la primera persona")

nombre1=input("Ingrese el nombre del producto: ")
precio1=int(input("Ingres un precio: "))
nombre2=input("Ingrese nombre del producto: ")
precio2=int(input("Ingrese un precio: " ))


BONIFICACION=20

precio_compra_total=precio1+precio2

comparar =precio1>=precio2
logico=(precio1>precio2 and precio1==precio2)

cabecera="resultados del producto {0}.  y del producto.{1}.: "
print (cabecera.format(nombre1,nombre2))

print ("el precio del primer valor es mayor o igual a el precio del segundo valor")
print(comparar)

print ("la suma de los dos productos es :" + str(precio_compra_total))
print ("precio1<precio2 and preci1=precio2")
print (logico)
precio_compra_total+=BONIFICACION
print("al precio total le incrementamos su valor que tiene la constante"+ str(precio_compra_total))