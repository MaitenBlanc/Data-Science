import pandas as pd

ruta = "./archivos/indicadores.csv"

df = pd.read_csv(ruta, sep=';')

print(f"Con valores nulos: \n{df['Anno2013']}")

df = df.dropna(subset=["Anno2013"])

print(f"Sin valores nulos: \n{df['Anno2013']}")