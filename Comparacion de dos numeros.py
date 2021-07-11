"""
Ingresar dos numeros y decir si el primero es mayor, menor o igual al segundo
"""

primer_numero = int(input("Ingrese el primer número: "))
segundo_numero = int(input("Ingrese el segundo número: "))

if(primer_numero > segundo_numero):
	print(f"{primer_numero} es mayor a {segundo_numero}")

elif(primer_numero == segundo_numero):
	print(f"{primer_numero} y {segundo_numero} son iguales")

else:
	print(f"{primer_numero} es menor a {segundo_numero}")