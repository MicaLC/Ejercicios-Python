"""
Cuando ingrese un número calcular su factorial
"""

numero_elegido = int(input("Ingrese un número: "))

while (numero_elegido <= 0):
	print("Los números negativos no tienen factorial. Elija un número mayor a 0\n")

	numero_elegido = int(input("Ingrese un número: "))
	
factorial = numero_elegido

contador = numero_elegido

while(contador > 1):
	factorial = factorial * (contador - 1)

	contador = contador - 1 

print(f"El factorial de {numero_elegido} es {factorial}")