import pandas as pd

df = pd.read_csv("C:/Users/maite/OneDrive/Escritorio/Curso-NTT/Area_3/3.4/archivos/Esculturas_Parque_Arqueolgicos_Colombia.csv", sep=",")

data = df.iloc[105]

print(f"Datos del registro 105: \n{data} \n")

nombre = data['Nombre elemento arqueológico']

print(f"Nombre del elemento del registro 105: {nombre}")




