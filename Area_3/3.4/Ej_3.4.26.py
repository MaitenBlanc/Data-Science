import pandas as pd

data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
            'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'Pedidos': [20, 40, None, 25, 10, 35, None, None, 22, 42, 36, None],
    'Facturación': [15000, 30000,2500, None, 25000, 30000, 1500, None, 15000, 35000, 25000, 2500],
    'Gastos': [5000, 6200, 4500, 3100, 5000, 5500, 6000, 5000, 6500, 5250, 7000, 5200],
    'Pendientes': [None, None, 25, None, 6, 15, 10, None, None, None, 4, None],
    'En_revisión': [None, None, None, None, 3, 5, 2, None, 1, None, None, 1]
}
df = pd.DataFrame(data)

nulos = df.isnull().sum()

media_nulos = df.isnull().mean()

data_null = {
    'Nulos': nulos,
    'Media nulos': media_nulos
}
df = pd.DataFrame(data_null)

print(df)