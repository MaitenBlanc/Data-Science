from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

notas = {
    "Lengua": [5, 7, 6, 2, 8, 9, 3, 4, 1, 9, 5, 4, 6, 4, 8, 7, 6, 2, 8, 9],
    "Inglés": [7, 9, 7, 5, 9, 9, 5, 6, 3, 9, 7, 6, 8, 6, 9, 8, 8, 4, 9, 9]
}

x = np.array(notas["Lengua"])
y = np.array(notas["Inglés"])

# Gráfico de dispersión
plt.scatter(x, y)
plt.xlabel("Lengua")
plt.ylabel("Inglés")
sns.regplot(x = x, y = y)
plt.title("Correlación Lengua e Inglés")
plt.grid();
plt.show()

# Correlación
correlacion = np.corrcoef(x, y)
print(f"Valor de correlación: {correlacion[0][1]}")



