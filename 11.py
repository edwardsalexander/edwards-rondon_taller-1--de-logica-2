#Invertir un número: Recorre los dígitos de un número desde el principio hasta
#el final utilizando un ciclo for y constrúyelo en orden inverso

numero = 2005
lista = str(numero)
invertido = ""

for digito in lista:
    invertido = digito + invertido

invertido = int(invertido)
print(f"el numero ingresado es:{numero} invertido es: {invertido}")