import pandas as pd
from sklearn.svm import SVR
from sklearn.feature_selection import RFE

ruta = "./archivos/Tabla.csv"

df = pd.read_csv(ruta, sep=";")

estimador = SVR(kernel = 'linear')

selector = RFE(estimador, step=1)
selector = selector.fit(X = df.loc[:, df.columns != 'A'], y = df['A'])

print(f"{selector.support_}\n{selector.ranking_}")