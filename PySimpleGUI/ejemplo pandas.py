import pandas as pd

datos = pd.read_csv("Adquisiciones_realizadas.csv")

# print(datos)

# Tomamos las primeras 10 filas
print(datos.head(10))

# Tomamos las últimas 7 filas
print(datos.tail(7))

# Tomamos una sola columna
print(datos[" Monto_Total_Sin_IVA "])

# Suma total
suma = datos[" Monto_Total_Sin_IVA "].sum()
print(f"Suma total: {suma:,.2f}")

# Promedio
promedio = datos[" Monto_Total_Sin_IVA "].mean()
print(f"Promedio: {promedio:,.2f}")

# Máximo
maximo = datos[" Monto_Total_Sin_IVA "].max()
print(f"Máximo: {maximo:,.2f}")

# Mínimo
minimo = datos[" Monto_Total_Sin_IVA "].min()
print(f"Mínimo: {minimo:,.2f}")

# Desviación estándar
std = datos[" Monto_Total_Sin_IVA "].std()
print(f"Desviación estándar: {std:,.2f}")

print(datos.columns.to_list())