import pandas as pd

ruta = "C:/Users/maite/OneDrive/Escritorio/Curso-NTT/Area_3/3.5/archivos/indicadores.csv"

df = pd.read_csv(ruta, sep=';')

nulos = df.isnull().sum()
print(f"Elementos nulos de cada variable: \n{nulos}")