from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

ruta = "./archivos/Tabla.csv"

df = pd.read_csv(ruta, sep=";")

plt.figure(figsize = (12, 4))

corr = df.corr()

sns.heatmap(corr, cmap="Blues", annot=True, fmt='.2f')

plt.show()