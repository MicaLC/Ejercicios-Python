"""
Perdirle al usuario una contraseña que sea "empanada" con 3 intentos
"""

contraseña = "empanada"

intentos = 3

while(intentos > 0):

	ingreso = input("Ingrese la contraseña: ")

	if(ingreso == contraseña):
		print( "Bienvenido")

		break

	else:
		print( "La contraseña es incorrecta\n")
		intentos = intentos - 1

		if(intentos == 0):
			print("Se le agotaron los intentos")
