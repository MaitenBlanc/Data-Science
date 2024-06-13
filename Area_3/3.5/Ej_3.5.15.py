from matplotlib import pyplot as plt
import pandas as pd

ruta = "./archivos/indicadores.csv"
df = pd.read_csv(ruta, sep=';')

cols = ['Anno2014', 'Anno2016']

Q1 = df[cols].quantile(0.25)
Q3 = df[cols].quantile(0.75)
RI = Q3 - Q1

for columna in cols:
    filter_outliers = (df[columna] < (Q1[columna] - 1.5*RI[columna])) | (df[columna] > (Q3[columna] + 1.5*RI[columna]))
    df = df[~filter_outliers]

df.boxplot(column=cols,
        patch_artist=True,
        flierprops=dict(markerfacecolor='orange'),
        boxprops=dict(facecolor='lightblue'))

plt.title("Outliers en los años 2014 y 2016")

plt.show()