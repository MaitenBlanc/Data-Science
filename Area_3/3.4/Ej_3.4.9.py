import pandas as pd

df = pd.read_csv('./archivos/ejecucion-presupuestaria_Chile-febrero-2023.csv', sep=';')

df_nuevo = df.loc[:, ["Nombre_Subtítulo", "Ejecución_de_FEBRERO"]]

print(df_nuevo)