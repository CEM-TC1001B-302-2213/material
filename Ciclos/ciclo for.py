
# range(número) -> Genera una secuencia numérica que inicia en 0,
# termina uno antes de número y avanza de 1 en 1
for i in range(5):
    print(f"El valor de i es: {i}")
    
print("-------------------")

# range(inicio, final) -> Genera una secuencia numérica que inicia en inicio,
# termina uno antes de final y avanza de 1 en 1
for i in range(5,10):
    print(f"El valor de i es: {i}")
    
print("-------------------")

# range(inicio, final, paso) -> Genera una secuencia numérica que inicia en inicio,
# termina antes de final y avanza de paso en paso
for i in range(5,21,3):
    print(f"El valor de i es: {i}")
    
print("-------------------")

for i in range(10, 5, -1):
    print(f"El valor de i es: {i}")
    
print("-------------------")

texto = "Hola mundo"
for i in texto:
    print(f"El valor de i es: {i}")
    
print("-------------------")

lista = [5, 8.6, True, "texto", [1,2,3], (17,4,2)]
for i in lista:
    print(f"El valor de i es: {i}")