#Verificación de número primo:
# Usa un ciclo for para verificar si un número es divisible por algún número entre 2 y su raíz cuadrada.
# Si no tiene divisor es primo

numero = int(input("ingresar el numero :"))
numero_str = str(numero)
es_primo = True
for i in range(len(numero_str) // 2):
    if numero[i] % 2 ==  0:
        es_primo == False 
    break

print(f"el numero {numero_str} es primo {es_primo}")