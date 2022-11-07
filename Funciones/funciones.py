
# Sin parámetros
# Sin valor de retorno
def suma1():
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    resultado = a + b
    print(f"El resultado de la suma es: {resultado}")
    
# Sin parámetros
# Con valor de retorno
def suma2():
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    resultado = a + b
    return resultado

# Con parámetros
# Con valor de retorno
def suma3(a, b):
    resultado = a + b
    return resultado

# suma1()
# salida = suma2()
# print(salida)

salida = suma3(7, 9)
print(salida)

x = float(input("Ingresa a: "))
y = float(input("Ingresa b: "))
salida = suma3(x, y)
print(salida)

operacion = suma3(30, 15) + 18 / 2 - 25
print(operacion)
    