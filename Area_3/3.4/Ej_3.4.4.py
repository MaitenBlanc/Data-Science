import pandas as pd

df = pd.read_csv("./archivos/Esculturas_Parque_Arqueolgicos_Colombia.csv", sep=",")

df_impares = df[df.index % 2 != 0]

print(df_impares)

print(f"\nCantidad de registros: {df_impares.shape[0]}")
    
    
    