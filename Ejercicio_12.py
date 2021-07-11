"""
Ingresar dos numeros, y continuar hasta que el útlimo sea menor o igual al anterior
"""

primer_numero = int(input("Ingrese el primer número: "))
segundo_numero = int(input("Ingrese el segundo número: "))

while(primer_numero < segundo_numero):
	primer_numero = segundo_numero
	segundo_numero = int(input("\nIngrese otro número: "))

print("Game over")
