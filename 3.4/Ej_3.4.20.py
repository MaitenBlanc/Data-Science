import pandas as pd

datos = {'Mes':['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
        'Ventas':[10000, 15200, 14300, 25800, 2560, 12780, 32500, 23624, 12000, 15858, 23250, 11630],
        'Gastos':[6500, 6500, 6500, 7850, 6500, 8250, 6500, 9252, 6500, 10250, 12450, 13000],
        'Beneficio':[3500,8700,7800,17950,-3940,4530,26000,14372,5500,5608,10800,-1370],
        'Cobrado':['S', 'N', 'N', 'S', 'S', 'N', 'S', 'S', 'S', 'N', 'S', 'N']}

df = pd.DataFrame(datos)

df["Dividendo"] = df["Beneficio"]

df = df.assign(Dividendo = df['Dividendo'] * 0.1)

df['Dividendo'] = df['Dividendo'].map(lambda x: 0 if x < 0 else x)

# Ej 20
df['Porcentaje_Dividendo'] = (df['Dividendo'] / df['Ventas']) * 100

df = round(df.assign(Porcentaje_Dividendo = df['Porcentaje_Dividendo']), 2)

print(df)