import pandas as pd

df = pd.read_csv("./archivos/Esculturas_Parque_Arqueolgicos_Colombia.csv", sep=",")

df_nuevo = df.set_index('Elemento arqueológico')

mostrar_elem = df_nuevo.loc['Sarcófago']

print(mostrar_elem)

print(f"\nHay {mostrar_elem.shape[0]} elementos.")