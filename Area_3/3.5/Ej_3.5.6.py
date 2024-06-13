import pandas as pd
import matplotlib.pyplot as plt

ruta = "./archivos/World_Development_Report_2021.csv"
df = pd.read_csv(ruta, sep=',')

boxplot = df.boxplot()

plt.show()