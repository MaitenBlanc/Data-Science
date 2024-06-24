import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier

ruta = "./archivos/Tabla.csv"

df = pd.read_csv(ruta, sep=";")

model = ExtraTreesClassifier()

model.fit(X = df.loc[:, df.columns != "D"], y = df["D"])

print(model.feature_importances_)