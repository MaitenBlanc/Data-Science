import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

arr1 = a*6
arr2 = b*6

c = np.array([arr1, arr2])

print(f"{c} -> tiene {c.shape} filas y columnas y el tipo de datos es {c.dtype}")