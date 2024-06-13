import pandas as pd

ruta = "./archivos/World_Development_Report_2021.csv"
df = pd.read_csv(ruta, sep=',')

df_tipo_datos = df.dtypes

print(df_tipo_datos)