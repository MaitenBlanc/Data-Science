import pandas as pd

data = {
    "Mes": ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'],
    "Importes Facturados": [10000, 15200, 14300, 25800, 2560, 12780, 32500, 23624, 12000, 15858, 23250, 11630],
    "Gastos": [6500, 6500, 6500, 7850, 6500, 8250, 6500, 9252, 6500, 10250, 12450, 13000],
    "Cobrado": ['S', 'N', 'N', 'S', 'S', 'N', 'S', 'S', 'S', 'N', 'S', 'N']
}

df = pd.DataFrame(data)

# Pregunta 1: ¿Cuántas filas tiene el dataframe?
print(f"Cantidad de filas: {df.shape[0]}")

# Pregunta 2: ¿Cuáles son las columnas que los forman?
print(f"Columnas: {df.columns.values}")

# Pregunta 3: ¿Cuánto espacio ha utilizado en memoria?
print(f"Memoria usada en cada columna: \n{df.memory_usage(deep=True)}")

# Pregunta 4: ¿Cuál es la media de las ventas anuales?
media = df['Importes Facturados'].mean().round(2)
print(f"Media de las ventas anuales: ${media}")

# Pregunta 5: Teniendo en cuenta solo las columnas Ventas y Gastos, al final de año, ¿crees que la empresa es rentable?
rentabilidad = (df['Importes Facturados'] - df['Gastos']).sum()
print(f"Rentabilidad: ${rentabilidad} \n La empresa es rentable ya que la diferencia es positiva.")