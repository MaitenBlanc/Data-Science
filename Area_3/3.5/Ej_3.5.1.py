import pandas as pd

ruta = "C:/Users/maite/OneDrive/Escritorio/Curso-NTT/Area_3/3.5/archivos/World_Development_Report_2021.csv"
df = pd.read_csv(ruta, sep=',')

df_tipo_datos = df.dtypes

print(df_tipo_datos)