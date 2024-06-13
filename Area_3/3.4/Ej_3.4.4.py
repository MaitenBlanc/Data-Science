import pandas as pd

df = pd.read_csv("C:/Users/maite/OneDrive/Escritorio/Curso-NTT/Area_3/3.4/archivos/Esculturas_Parque_Arqueolgicos_Colombia.csv", sep=",")

df_impares = df[df.index % 2 != 0]

print(df_impares)

print(f"\nCantidad de registros: {df_impares.shape[0]}")
    
    
    