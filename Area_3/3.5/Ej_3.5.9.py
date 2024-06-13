import pandas as pd

ruta = "./archivos/indicadores.csv"

df = pd.read_csv(ruta, sep=';')

nulos = df.isnull().sum()
print(f"Elementos nulos de cada variable: \n{nulos}")