import pandas as pd

df = pd.read_csv("C:/Users/maite/OneDrive/Escritorio/Curso-NTT/Area_3/3.4/archivos/Esculturas_Parque_Arqueolgicos_Colombia.csv", sep=",")

df_nuevo = df.set_index('Elemento arqueológico')

df_sarcofago = df_nuevo.loc['Sarcófago']

df_sarcofago = df_sarcofago.reset_index()

print(df_sarcofago['Parque Arqueologico'].head(3))


