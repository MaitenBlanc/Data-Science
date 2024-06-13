import pandas as pd

df = pd.read_csv('./archivos/ejecucion-presupuestaria_Chile-febrero-2023.csv', sep=';')

saldo = 10000000
mayor_10000000 = df[(df['Ejecución_a_FEBRERO'] > saldo) & (df['Moneda'] == "PESOS")]

mostrar = mayor_10000000.loc[:, ['Subtítulo', 'Ejecución_a_FEBRERO']]

print(mostrar)