dinero_para_invertir = int( input("Ingrese el monto a invertir: $"))
interes_anual = float( input("Ingrese el interés anual: "))
años = int( input( "Ingrese la cantidad de años a invertir: "))
contador = años

while(contador > 0):

	dinero_en_un_año = dinero_para_invertir * interes_anual

	dinero_para_invertir = dinero_para_invertir + dinero_en_un_año

	contador = contador - 1

print(f"Luego de {años} años vas a ganar en total {dinero_para_invertir}")