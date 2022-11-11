
# for i in range(1,11):

i = 1 # Variable de control (contador)
while i <= 10: # Condición de paro o de salida
    print(f"El valor de i es: {i}")
    i = i + 1 # Paso o incremento al contador
    
print("----------------------------")

# Mostrar los impares del 3 al 21 -> 3,5,7,9,...,21
i = 3
while i <= 21:
    print(f"El valor de i es: {i}")
    i = i + 2
    
print("----------------------------")

# for i in texto:
texto = "hola mundo"
i = 0
while i < len(texto):
    print(f"El valor de texto[{i}] = {texto[i]}")
    i = i + 1

print("----------------------------")

#for i in lista:
lista = [1.5, 7, True, [1,2,3], "hola"]
i = 0
while i < len(lista):
    print(f"El valor de lista[{i}] = {lista[i]}")
    i = i + 1

print("----------------------------")

# Duda aparte
# Dividir el texto en palabras
texto = "Ya por fin es viernes"
lista = texto.split()
for i in lista:
    print(i)

print("----------------------------")

# Ejemplo de un ciclo indefinido
centinela = "n"
while centinela != "s":
    centinela = input("¿Desea terminar (s/n)?: ")
