import pandas as pd

ruta = "C:/Users/maite/OneDrive/Escritorio/Curso-NTT/Area_3/3.5/archivos/indicadores.csv"

df = pd.read_csv(ruta, sep=';')

for columna in df.columns:
    if df[columna].dtype != 'object':
        media = round(df[columna].mean(), 2)
        df[columna].fillna(media, inplace=True)

print(f"{df.isnull().sum()}\n")

print(df)