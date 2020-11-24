print	("Velocidad=d/t")
distancia=int(input("Digite la distancia que debe recorrer :"))
velocidad=int(input("Digite la velocidad : "))
tiempo=distancia/velocidad
cabecera = "el tiempo en recorrer {0} km a una velocidad {1} km/h es igual	{2} " 
print (cabecera.format (distancia,velocidad,tiempo) )