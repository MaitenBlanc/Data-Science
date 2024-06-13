import pandas as pd

ruta = "./archivos/World_Development_Report_2021.csv"
df = pd.read_csv(ruta, sep=',')

duplicados = df[df.duplicated(subset=['census_round','counted','population','percentage'], keep=False)]

print(f"Filas duplicadas: \n{duplicados}\n")
print(f"Cantidad de filas duplicadas: {df.duplicated().sum()}")