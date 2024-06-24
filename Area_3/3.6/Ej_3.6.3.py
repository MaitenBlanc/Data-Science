import pandas as pd
from sklearn.preprocessing import Normalizer

data = {
    'Ventas':[10000, 15200, 14300, 25800, 2560, 12780, 32500, 23624, 12000, 15858, 23250, 11630],
    'Gastos':[6500, 6500, 6500, 7850, 6500, 8250, 6500, 9252, 6500, 10250, 12450, 13000],
    'Beneficio':[3500,8700,7800,17950,-3940,4530,26000,14372,5500,5608,10800,-1370]
}
df = pd.DataFrame(data)

scaler = Normalizer().fit(df)
normalizedX = scaler.transform(df)

df = pd.DataFrame(normalizedX, columns=df.columns)

print(f"DataFrame con las variables normalizadas: \n{df}")