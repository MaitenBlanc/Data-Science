import pandas as pd

df = pd.read_csv("./archivos/Esculturas_Parque_Arqueolgicos_Colombia.csv", sep=",")

datos = df.loc[100:110, "Código ICANH"]

print(f"Datos: \n{datos}")


