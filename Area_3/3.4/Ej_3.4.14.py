import pandas as pd

df = pd.read_csv('./archivos/ejecucion-presupuestaria_Chile-febrero-2023.csv', sep=';')

lista = ["IMPUESTOS","RENTAS DE LA PROPIEDAD","INGRESOS DE OPERACIÓN","VENTA DE ACTIVOS FINANCIEROS"]

saldo = 10000
df_lista = df.loc[(df["Ejecución_de_FEBRERO"] > saldo) &
                (df["Moneda"] == 'DOLARES') &
                (df["Nombre_Subtítulo"].isin(lista))
                ]

print(df_lista)