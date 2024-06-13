import pandas as pd

df = pd.read_csv("./archivos/Esculturas_Parque_Arqueolgicos_Colombia.csv", sep=",")

datos = df.loc[[24, 36, 125, 182], ["Nombre elemento arqueológico", "Ubicación actual dentro del parque"]]

print(f"Datos de los registros: \n{datos}\n")

misma_ubicacion = datos[datos.duplicated('Ubicación actual dentro del parque')]

if misma_ubicacion.empty:
    print("No existen elementos en la misma ubicación.")
else:
    print(f"Hay elementos en la misma ubicación: \n{misma_ubicacion['Ubicación actual dentro del parque']}")