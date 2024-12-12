#Suma de los primeros n números naturales:
#Calcula la suma de los números desde 1 hasta n utilizando un ciclo for.
#Itera sobre los números en el rango de 1 a n y acumula su suma.
counter = 0
adder = 0
 
for numero in range(1, 11):
    counter += 1
    adder +=  numero
    print(f"los numero a sumar son: {counter}")
print(f"la suma de estos numero es: {adder}")    
    
