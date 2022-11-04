udf1 = float(input("Introduce tu calificación de tu udf1: "))
udf2 = float(input("Introduce tu calificación de tu udf2: "))
udf3 = float(input("Introduce tu calificación de tu udf3: "))
udf4 = float(input("Introduce tu calificación de tu udf4: "))
udf5 = float(input("Introduce tu calificación de tu udf5: "))
udf6 = float(input("Introduce tu calificación de tu udf6: "))
udf7 = float(input("Introduce tu calificación de tu udf7: "))

promedio = (udf1 + udf2 + udf3 + udf4 + udf5 + udf6 + udf7) / 7

print("El promedio de tu semestre fue:", promedio, "Estudia más.")
print("El promedio de tu semestre fue: " + str(promedio) + " Estudia más.")
print("El promedio de tu semestre fue: {0:,.2f} Estudia más.".format(promedio))
print(f"El promedio de tu semestre fue: {promedio:,.2f} Estudia más.")