import pandas as pd

df = pd.read_csv("./archivos/Esculturas_Parque_Arqueolgicos_Colombia.csv", sep=",")

df_nuevo = df.set_index('Elemento arqueológico')

df_sarcofago = df_nuevo.loc['Sarcófago']

df_sarcofago = df_sarcofago.reset_index()

print(df_sarcofago['Parque Arqueologico'].head(3))


