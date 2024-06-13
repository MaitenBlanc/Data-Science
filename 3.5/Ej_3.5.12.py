import pandas as pd

ruta = "C:/Users/maite/OneDrive/Escritorio/Curso-NTT/Area_3/3.5/archivos/indicadores.csv"

df = pd.read_csv(ruta, sep=';')

print(f"Con valores nulos: \n{df['Anno2013']}")

df = df.dropna(subset=["Anno2013"])

print(f"Sin valores nulos: \n{df['Anno2013']}")

