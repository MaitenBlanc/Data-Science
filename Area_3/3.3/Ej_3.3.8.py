from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

notas = {
    "Lengua": [5, 7, 6, 2, 8, 9, 3, 4, 1, 9, 5, 4, 6, 4, 8, 7, 6, 2, 8, 9],
    "Matemática": [7, 8, 5, 6, 8, 3, 2, 9, 9, 6, 1, 5, 7, 3, 5, 4, 5, 9, 7, 6]
}

x = np.array(notas["Lengua"])
y = np.array(notas["Matemática"])

# Gráfico de dispersión
plt.scatter(x, y)
plt.xlabel("Lengua")
plt.ylabel("Matematicas")
sns.regplot(x = x, y = y)
plt.title("Correlación Lengua y Matematicas")
plt.grid();
plt.show()

# Correlación
correlacion = np.corrcoef(x, y)
print(f"Valor de correlación: {correlacion[0][1]}")