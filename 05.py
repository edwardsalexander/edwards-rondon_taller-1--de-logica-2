#Tabla de multiplicar de un número:
# Genera la tabla de multiplicar de un número dado del 1 al 10 utilizando un ciclo for.
# Por cada iteración, calcula el producto y muéstralo.

multiplicador = int(input("ingrese el numero que desea saber la tabla de multiplicar"))
resultado = 1

for numero in range(1, 11):
    multiplicador * numero
    resultado = multiplicador * numero  
    print(multiplicador, "*", numero , "=", resultado) 

   
