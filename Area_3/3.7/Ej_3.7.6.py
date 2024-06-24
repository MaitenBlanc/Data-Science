import pandas as pd

data = {
    'nombre': ['Luis Zafra', 'Gemma Sanz', 'Lourdes Mora', 'Isaac Pérez', 'Sonia Gracia', 'Alberto Lungo', 'Tamara López'],
    'fecha_nacimiento': ['15/05/1993', '25/04/2000', '04/12/1985', '18/10/1999', '02/08/2001', '11/11/1986', '06/07/1991'],
    'zona': [0, 2, 1, 3, 0, 1, 1],
    'articulo': [348, 125, 3, 248, 124, 17 ,157],
    'cantidad': [1, 3, 2, 1, 1, 1, 2],
    'entregado': ['Sí', 'No', 'Sí', 'Sí', 'No', 'Sí', 'Sí'],
    'metodo_pago': ['Tarjeta', 'Transferencia', 'Bizum', 'Tarjeta', 'Tarjeta', 'Transferencia', 'Contrareembolso'],
    "dto": ['No', 'Sí', 'No', 'No', 'No', 'Sí', 'Sí']
}
df = pd.DataFrame(data)

df["fecha_nacimiento"] = pd.to_datetime(df["fecha_nacimiento"], format='%d/%m/%Y')

prioridad = {0: 1, 1: 2, 2: 3, 3: 4}
df.insert(3, 'prioridad', 0)
df['prioridad'] = df['zona'].map(prioridad).astype("category")

df["entregado"] = df["entregado"].map({'Sí': 1, 'No': 0}).astype("category")
df["dto"] = df["dto"].map({'Sí': 1, 'No': 0}).astype("category")

print(df)
print(df.info())