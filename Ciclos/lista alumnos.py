
lista = ["Nathan", "Abigail", "Oswald", "Camila", "Mariana"]

nombre = input("Ingrese el nombre a buscar: ")
encontrado = False
for i in lista:
    if nombre == i:
        encontrado = True
        
if encontrado:
    print(f"Se encontró a {nombre}.")
else:
    print(f"No se encontró a {nombre}.")


# ---------------------------

for i in lista:
    if nombre == i:
        print(f"Se encontró a {nombre}.")
        break # Rompe el ciclo, lo detiene prematuramente
else: # El else de un ciclo sólo se ejecuta si nunca se rompió el ciclo
    print(f"No se encontró a {nombre}.")