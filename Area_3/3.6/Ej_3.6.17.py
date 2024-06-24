import pandas as pd
from sklearn.feature_selection import VarianceThreshold

ruta = "./archivos/Tabla.csv"

df = pd.read_csv(ruta, sep=";")

var_th = VarianceThreshold(threshold = 0.5)

x_var = var_th.fit_transform(df)

print(f"Número de características generales: {df.shape[1]}")
print(f"Número de características finales: {x_var.shape[1]}")
print(f"Listado de características originales: {df.columns}")
print(f"Listado de características finales: {df.columns[var_th.get_support()]}")