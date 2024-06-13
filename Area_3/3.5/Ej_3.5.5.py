import pandas as pd

ruta = "./archivos/World_Development_Report_2021.csv"
df = pd.read_csv(ruta, sep=',')

minimo = df['percentage'].min()
maximo = df['percentage'].max()
media = df['percentage'].mean()

print(f"Valor mínimo de percentage: {minimo}")
print(f"Valor máximo de percentage: {maximo}")
print(f"Media de percentage: {media}")