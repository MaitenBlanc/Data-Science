import pandas as pd

data = {
    'Mes':['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
    'Pedidos': [20, 40, None, 25, 10, 35, None, None, 22, 42, 36, None],
    'Facturación': [15000, 30000,2500, None, 25000, 30000, 1500, None, 15000, 35000, 25000, 2500],
    'Gastos': [5000, 6200, 4500, 3100, 5000, 5500, 6000, 5000, 6500, 5250, 7000, 5200],
    'Pendientes': [None, None, 25, None, 6, 15, 10, None, None, None, 4, None],
    'En_revisión': [None, None, None, None, 3, 5, 2, None, 1, None, None, 1]
}

datos2 = {
    "Mes":["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
    "Pedidos":[10,20,15,None,10,None,26,12,None,22,42,36],
    "Facturas":[6500,25000,15000,12000,None,10000,10500,None,15000,15000,5000,25000],
    "Gastos":[5000,6200,4500,3100,5000,5500,6000,5000,6500,5250,7000,5200],
    "Pendientes":[None,None,5,3,6,15,10,None,None,None,4,None],
    "En_revision":[None,None,2,None,3,5,2,None,1,None,1,1]
}

df = pd.DataFrame(data)
df2 = pd.DataFrame(datos2)

df_concat = pd.concat([df,df2])

df_concat = df_concat.reset_index()
print(df_concat)