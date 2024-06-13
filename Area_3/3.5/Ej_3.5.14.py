from matplotlib import pyplot as plt
import pandas as pd

ruta = "./archivos/indicadores.csv"
df = pd.read_csv(ruta, sep=';')

df.boxplot(column=["Anno2014", "Anno2016"],
        patch_artist=True,
        flierprops=dict(markerfacecolor='orange'),
        boxprops=dict(facecolor='lightblue'))

plt.title("Outliers en los años 2014 y 2016")

plt.show()