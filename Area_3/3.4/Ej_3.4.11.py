import pandas as pd

df = pd.read_csv('./archivos/ejecucion-presupuestaria_Chile-febrero-2023.csv', sep=';')

mayor_20000 = df[(df['Ejecución_de_FEBRERO'] > 20000) & (df['Moneda'] == "DOLARES")]

print(f"Registros mayores a 20000 dólares: \n{mayor_20000}")