#medida de una lista de numeros: recorrer cada numero de una lista 
#con un ciclo for, acumula su suma y divide entre el numero total 
# de elementos para calcular media.

numero_lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
suma = 0

for numero in numero_lista:
    suma += numero 
    medida = suma / len(numero_lista )
     
print(medida)    
    
    
