import pandas as pd

df = pd.read_csv("C:/Users/maite/OneDrive/Escritorio/Curso-NTT/Area_3/3.4/archivos/Esculturas_Parque_Arqueolgicos_Colombia.csv", sep=",")

ubicacion = df.loc[[10, 20, 30, 40, 50], 'Ubicación actual dentro del parque']

print(f"Datos: \n{ubicacion}")