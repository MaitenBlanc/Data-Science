import pandas as pd

df = pd.read_csv("./archivos/Esculturas_Parque_Arqueolgicos_Colombia.csv", sep=",")

data = df.iloc[105]

print(f"Datos del registro 105: \n{data} \n")

nombre = data['Nombre elemento arqueológico']

print(f"Nombre del elemento del registro 105: {nombre}")