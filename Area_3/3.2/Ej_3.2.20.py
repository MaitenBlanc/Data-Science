import pandas as pd

data = {
    "Mes": ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'],
    "Importes Facturados": [10000, 15200, 14300, 25800, 2560, 12780, 32500, 23624, 12000, 15858, 23250, 11630],
    "Gastos": [6500, 6500, 6500, 7850, 6500, 8250, 6500, 9252, 6500, 10250, 12450, 13000],
    "Cobrado": ['S', 'N', 'N', 'S', 'S', 'N', 'S', 'S', 'S', 'N', 'S', 'N']
}

df = pd.DataFrame(data)

df["Beneficio"] = 0

print(df)