import pandas as pd

df = pd.read_csv("./archivos/Esculturas_Parque_Arqueolgicos_Colombia.csv", sep=",")

ubicacion = df.loc[[10, 20, 30, 40, 50], 'Ubicación actual dentro del parque']

print(f"Datos: \n{ubicacion}")