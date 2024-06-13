import pandas as pd

df = pd.read_csv("./archivos/Esculturas_Parque_Arqueolgicos_Colombia.csv", sep=",")

df_nuevo = df.set_index('Elemento arqueológico')

print(df_nuevo)