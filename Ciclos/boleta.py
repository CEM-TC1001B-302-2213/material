udfs = int(input("Ingresa el número de unidades de formación: "))
promedio = 0

for i in range(1, udfs+1):
    udf = float(input(f"Introduce tu calificación de tu udf{i}: "))
    promedio = promedio + udf

promedio = promedio / udfs

print(f"El promedio de tu semestre fue: {promedio:,.2f}")

if promedio > 90:
    print("Excelente semestre.")
elif promedio >= 80:
    print("Fue un buen semestre.")
else:
    print("Estudia más.")