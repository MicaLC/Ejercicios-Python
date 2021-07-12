"""
Crear una función que sume dos números,
una que los reste,
una que los multiplique,
una que los divida,
y otra que las factorice
"""

def sumar(num1, num2):
	return num1 + num2

def restar(num1, num2):
	return num1 - num2

def multiplicar(num1, num2):
	return num1 * num2

def dividir(num1, num2):
	return num1 / num2

def factorial(num1, num2):
	for i in range(2):
		if(i == 0):
			contador = num1 - 1
			while(contador > 0):
				num1 = num1 * contador
				contador = contador - 1

		else:
			contador = num2 - 1
			while(contador > 0):
				num2 = num2 * contador
				contador = contador - 1

	return [num1, num2]

def datos():
	return int(input("Ingrese un valor: "))

def menu():
	opcion = int(input("Ingrese el número de la función que quiere realizar:\n1-Suma\n2-Resta\n3-Multiplicación\n4-División\n5-Factorial\n"))
	print()

	if(opcion == 1):
		print("El resultado es: ", sumar(datos(), datos()))

	elif(opcion == 2):
		print("El resultado es: ", restar(datos(), datos()))

	elif(opcion == 3):
		print("El resultado es: ", multiplicar(datos(), datos()))

	elif(opcion == 4):
		print("El resultado es: ", dividir(datos(), datos()))

	elif(opcion == 5):
		numero1 = datos()
		numero2 = datos()
		factorizar = factorial(numero1, numero2)

		for i in range(2):
			if(i == 0):
				print(f"\nEl resultado de {numero1} es: ",factorizar[i])
			else:
				print(f"\nEl resultado de {numero2} es: ",factorizar[i])

	else:
		print("Por favor elija una de las opciones\n")
		menu()

menu()
