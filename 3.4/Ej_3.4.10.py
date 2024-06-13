import pandas as pd

df = pd.read_csv('C:/Users/maite/OneDrive/Escritorio/Curso-NTT/Area_3/3.4/archivos/ejecucion-presupuestaria_Chile-febrero-2023.csv', sep=';')

negativos = df[df['Ejecución_de_FEBRERO'] <= 0]

print(f"Condicional simple: \n{negativos} \n")

datos = negativos.loc[:, ["Nombre_Subtítulo", "Ejecución_de_FEBRERO"]]

print(f"Muestra nombre y ejecución Febrero: \n{datos}")