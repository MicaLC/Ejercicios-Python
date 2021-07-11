"""
Calcular la tabla de un número
"""

numero_elegido = int(input("Ingrese un número: "))

multiplicador = 1 

while(multiplicador <= 10):
	print(f"{numero_elegido} por {multiplicador} es {numero_elegido * multiplicador}")

	multiplicador = multiplicador + 1
