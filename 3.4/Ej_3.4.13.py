import pandas as pd

df = pd.read_csv('C:/Users/maite/OneDrive/Escritorio/Curso-NTT/Area_3/3.4/archivos/ejecucion-presupuestaria_Chile-febrero-2023.csv', sep=';')

lista = ["IMPUESTOS","RENTAS DE LA PROPIEDAD","INGRESOS DE OPERACIÓN","VENTA DE ACTIVOS FINANCIEROS"]

df_lista = df.loc[df["Nombre_Subtítulo"].isin(lista)]

print(df_lista)