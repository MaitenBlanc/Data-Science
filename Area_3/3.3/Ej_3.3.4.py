import numpy as np

datos = np.array([0] * 5 + [1] * 6 + [2] * 8 + [3] * 4 + [4] * 2)

print(f"Media: {np.mean(datos)}")
print(f"Varianza: {np.var(datos)}")