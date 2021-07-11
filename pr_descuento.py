#un juego con descuento y si es menor a 100 se compra

precio = int(input("ingrese el precio: "))

descuento = float(input("ingrese el descuento: "))
if(descuento <= 100):
	
	multiplicador = descuento /100
	
	resto = precio * multiplicador
	
	precio_final = precio - resto
	
	if(precio_final <= 100):
		print("Es momento de comprarlo, sólo te sale: ", precio_final)

	elif(precio_final <= 200):
		print("No esta barato, pero si de todas formas lo queres comprar te sale: ", precio_final)

	elif(precio_final <= 300):
		print("No lo compres que te sale: ", precio_final)

	else:
		print("No vale la pena comprarlo, está: ", precio_final)

else:
	print("Ponga un número igual o menor a 100")
