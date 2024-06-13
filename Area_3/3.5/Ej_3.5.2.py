import pandas as pd

ruta = "C:/Users/maite/OneDrive/Escritorio/Curso-NTT/Area_3/3.5/archivos/World_Development_Report_2021.csv"
df = pd.read_csv(ruta, sep=',')

duplicados = df[df.duplicated(subset=['census_round','counted','population','percentage'], keep=False)]

print(f"Filas duplicadas: \n{duplicados}\n")
print(f"Cantidad de filas duplicadas: {df.duplicated().sum()}")