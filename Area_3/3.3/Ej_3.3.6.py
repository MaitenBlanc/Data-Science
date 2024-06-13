import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

datos = [
    [4, 5, 5, 1, 7, 4],
    [3, 2, 4, 4, 3, 6],
    [6, 4, 3, 3, 4, 5],
    [5, 2, 4, 7, 3, 6],
    [2, 1, 3, 7, 3, 1]
]

df = pd.DataFrame(datos)

corr_matriz = df.corr(method='pearson')

plt.figure(figsize=(8, 6))
plt.title("Mapa de correlación de Pearson")
sns.heatmap(corr_matriz, annot=True, cmap='coolwarm')
plt.show()