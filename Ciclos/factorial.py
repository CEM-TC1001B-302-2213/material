
n = int(input("Ingresa el valor de n: "))

factorial = 1
for i in range(1,n+1):
    factorial = factorial * i

print(f"El factorial de {n} es: {factorial}")