n = int(input("Ingresa el valor de n: "))

suma = 0
i = 1
while i <= n:
    suma = suma + i
    i = i + 1 # Se suele dejar la modificación al contador al final del ciclo
    

print(f"El resultado de la sumatoria es: {suma}")