import pandas as pd

df = pd.read_csv('./archivos/ejecucion-presupuestaria_Chile-febrero-2023.csv', sep=';')

saldo = 250000
df_diferencia = df[(df["Ejecución_a_FEBRERO"] - df["Ejecución_de_FEBRERO"] > saldo) &
                        (df["Moneda"] == "DOLARES")]

print(df_diferencia)