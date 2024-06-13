import pandas as pd

df = pd.read_csv("C:/Users/maite/OneDrive/Escritorio/Curso-NTT/Area_3/3.4/archivos/Esculturas_Parque_Arqueolgicos_Colombia.csv", sep=",")

datos = df.loc[100:110, "Código ICANH"]

print(f"Datos: \n{datos}")


