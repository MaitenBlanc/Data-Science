import pandas as pd

ruta = "./archivos/indicadores.csv"

df = pd.read_csv(ruta, sep=';')

df.drop(columns=["Anno1996", "Anno2001"], inplace=True)

print(df)