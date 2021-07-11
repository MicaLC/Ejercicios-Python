# 5 numeros y promedio
divisor = int( input("ingrese la cantidad de notas: "))
contador = divisor
acumulador = 0

if(divisor <= 0):
	print("Por favor ingrese un número mayor a 0")

else:
	while(contador > 0):
		numeros = int( input("ingrese la nota: "))
		acumulador = acumulador + numeros

		contador = contador - 1

	promedio = acumulador/divisor

	if(promedio >= 7):
		print("Promocionado con: ", promedio)

	elif(promedio >= 4):
		print( "Aprobado con", promedio, ", pero va a final")

	else:
		print("Recursa, se sacó: ", promedio)