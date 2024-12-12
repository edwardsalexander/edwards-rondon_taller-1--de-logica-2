#Suma de los dígitos de un número:
# Recorre cada dígito de un número (convirtiéndolo en una cadena de texto) y
# suma sus valores utilizando un ciclo for
cadena_de_numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
counter = 0
adder = 0

for numero in cadena_de_numeros:
    counter += 1
    adder +=  counter
    print(f" numero:{numero}")  
print(f"la suma de los numeros es: {adder}")

 
 