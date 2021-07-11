cantidad_de_numeros = int( input( "Ingrese la cantidad de números a restar: "))
numeros = int (input("Ingrese un número: "))
cantidad_de_numeros = cantidad_de_numeros -1

while(cantidad_de_numeros > 0):
	restar = int( input("Ingrese un número: "))
	numeros = numeros - restar
	
	cantidad_de_numeros = cantidad_de_numeros - 1

if(numeros >= 0):
	print(f"El resultado {numeros} es positivo")

else:
	print(f"El resultado {numeros} es negativo")
