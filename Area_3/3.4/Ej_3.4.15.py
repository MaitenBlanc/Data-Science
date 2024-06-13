import pandas as pd

df = pd.read_csv("./archivos/ejecucion-presupuestaria_Chile-febrero-2023.csv', sep=';')

df_3_9 = df.loc[:, ["Nombre_Subtítulo", "Ejecución_de_FEBRERO"]]

df_diferencia = df_3_9[(df["Ejecución_a_FEBRERO"] - df["Ejecución_de_FEBRERO"]) == 0]

print(df_diferencia)