"""
Calcular la tabla de un número utilizando "for"
"""

numero_elegido = int(input("Ingrese un número: "))

for i in range(1, 11):
	resultado = numero_elegido * i
	
	print(f"{numero_elegido} por {i} es {resultado}")
