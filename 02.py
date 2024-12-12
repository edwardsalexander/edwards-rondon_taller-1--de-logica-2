#Factorial de un número dado:
# Encuentra el factorial de un número multiplicando todos los números desde 1 hasta
# ese número con un ciclo for. Asegúrate de inicializar la variable acumuladora en 1

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

def calcular_factorial(numero):
    
    factorial = 1

    for numero in numeros:
        factorial *= numero
        
    return factorial

resultado =  calcular_factorial(numero = any )
numero = 10
print(f"la factorial del numero {numero} es :  {resultado}")
    
    

