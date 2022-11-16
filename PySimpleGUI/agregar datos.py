import pandas as pd

datos = pd.read_csv("Adquisiciones_realizadas.csv")

# "Nombre de la columna": valor
# "Numero_OC": values["input NUMERO_OC"]
nueva_fila = pd.DataFrame([{
    "Numero_OC": 12345,
    "Proveedor": "Mi proveedor",
    "Partida_Presupuestal": 54321,
    "Descripcion_de_la_Partida_ Presupuestal": "DESC",
    "Concepto": "Mi concepto",
    "Cantidad_Ordenada": 99999,
    "UM": "KG",
    " Monto_Total_Sin_IVA ": 9462,
    "Fundamentacion_legal": "ADJ DIRECTA"
    }])

datos = pd.concat([datos, nueva_fila], ignore_index=True)
datos.to_csv("Adquisiciones_realizadas.csv", index=False)
print("Terminó de guardar...")